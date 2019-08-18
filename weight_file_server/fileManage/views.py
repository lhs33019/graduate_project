from django.shortcuts import render
import os, mimetypes
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseNotFound
from django.conf import settings
from .models import WeightFile
from django.core import serializers
import datetime
from .forms import WeightFileForm

# Create your views here.
def getlist(request):
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
    
def send(request):
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

    
def download_direct(request, path):
    if request.method == 'GET':
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            response = HttpResponse(open(file_path, 'rb'), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            return response
        return HttpResponseNotFound('There is no file')
    else:
        return HttpResponseNotFound('Not valid request')

def download(request, file_id):
    if request.method == 'GET':
        weightFiles = WeightFile.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, weightFiles.weight_file.path)
        if os.path.exists(file_path):
            response = HttpResponse(open(file_path, 'rb'), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            return response
        return HttpResponseNotFound('There is no file')
    else:
        return HttpResponseNotFound('Not valid request')