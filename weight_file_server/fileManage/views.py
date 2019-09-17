from django.shortcuts import render
import os
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseNotFound
from django.conf import settings
from .models import WeightFile, ImageFile
from .forms import WeightFileForm, ImageFileForm
from django import db
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper


def download_direct(request, path):
    if request.method == 'GET':
        db.reset_queries()
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        filename = os.path.basename(file_path)
        chunk_size = 8192
        if os.path.exists(file_path):
            response = StreamingHttpResponse(
                FileWrapper(open(file_path, 'rb'), chunk_size),
                content_type="application/octet-stream"
            )
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            response['Content-Length'] = os.path.getsize(file_path)
            return response
        return HttpResponseNotFound('There is no file')
    else:
        return HttpResponseNotFound('Not valid request')

def getWeightList(request):
    if request.method == 'GET':
        weightFiles_list = list(WeightFile.objects.order_by('-created_at').values())

        # weightFiles_list = serializers.serialize('json', weightFiles)
        # weightFiles = serializers.serialize('json', [weightFiles.all()[0], ])
        # serialized_object = serializers.serialize('json', [WeightFile.objects.all(), ])

        return JsonResponse({
            'message' : 'Available Weight File List',
            'Weight Files' : weightFiles_list,
        }, json_dumps_params = {'ensure_ascii': True})

    else:
        return HttpResponseNotFound('Not valid request')
    
def sendWeight(request):
    if request.method == 'POST':
            form = WeightFileForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                form.save()
                print("valid")
                return HttpResponse(JsonResponse({'success': 'upload complete'}), status=202)
            else:
                print("unvalid")
    else:
        form = WeightFileForm()
        return render(request, 'upload.html', {'form': form})

    return HttpResponseNotFound('Not valid request')

def downloadWeight(request, file_id):
    if request.method == 'GET':
        db.reset_queries()
        weightFiles = WeightFile.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, weightFiles.weight_file.path)
        filename = os.path.basename(file_path)
        chunk_size = 8192
        if os.path.exists(file_path):
            response = StreamingHttpResponse(
                FileWrapper(open(file_path, 'rb'), chunk_size),
                content_type="application/octet-stream"
            )
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            response['Content-Length'] = os.path.getsize(file_path)
            return response
        return HttpResponseNotFound('There is no file')
    else:
        return HttpResponseNotFound('Not valid request')

# Create your views here.
def getImageList(request):
    if request.method == 'GET':
        imageFiles_list = list(ImageFile.objects.order_by('-created_at').values())

        # weightFiles_list = serializers.serialize('json', weightFiles)
        # weightFiles = serializers.serialize('json', [weightFiles.all()[0], ])
        # serialized_object = serializers.serialize('json', [WeightFile.objects.all(), ])

        return JsonResponse({
            'message' : 'Available Image File List',
            'Image Files' : imageFiles_list,
        }, json_dumps_params = {'ensure_ascii': True})

    else:
        return HttpResponseNotFound('Not valid request')

def downloadImage(request, file_id):
    if request.method == 'GET':
        db.reset_queries()
        imageFiles = ImageFile.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, imageFiles.image_file.path)
        filename = os.path.basename(file_path)
        chunk_size = 8192
        if os.path.exists(file_path):
            response = StreamingHttpResponse(
                FileWrapper(open(file_path, 'rb'), chunk_size),
                content_type="application/octet-stream"
            )
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            response['Content-Length'] = os.path.getsize(file_path)
            return response
        return HttpResponseNotFound('There is no file')
    else:
        return HttpResponseNotFound('Not valid request')

def sendImage(request):
    if request.method == 'POST':
            form = ImageFileForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                form.save()
                print("valid")
                return HttpResponse(JsonResponse({'success': 'upload complete'}), status=202)
            else:
                print("unvalid")
    else:
        form = ImageFileForm()
        return render(request, 'upload.html', {'form': form})

    return HttpResponseNotFound('Not valid request')