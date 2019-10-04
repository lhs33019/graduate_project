from django.shortcuts import render
import os
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.conf import settings
from .models import WeightFile, ImageFile
from .forms import WeightFileForm, ImageFileForm
from django import db
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper

# 파일에 대한 url로 서버에서 직접 다운로드 받을 때 호출
def download_direct(request, path):
    # GET 요청일 경우에만 응답
    if request.method == 'GET':
        db.reset_queries()
        # DB에 저장된 경로를 가져와 서버 내 파일의 물리 경로를 구한다
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        filename = os.path.basename(file_path)
        # 파일을 한번에 전송하는것은 부하가 커지므로 8192 바이트 단위로 끊어 스트림 방식으로 전송한다
        chunk_size = 8192
        if os.path.exists(file_path):
            # Response 헤더에 전송 타입, 파일의 크기, 보내는 파일의 이름을 설정해 응답한다.
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

# 현재 등록되어 사용 가능한 Weight 파일 리스트를 Json으로 응답
def getWeightList(request):
    # GET 요청일 경우에만 생성일의 내림차순으로 정렬한 list를 가져온다
    if request.method == 'GET':
        weightFiles_list = list(WeightFile.objects.order_by('-created_at').values())

        return JsonResponse({
            'message' : 'Available Weight File List',
            'Weight Files' : weightFiles_list,
        }, json_dumps_params = {'ensure_ascii': True})

    else:
        return HttpResponseNotFound('Not valid request')

# Weight 파일을 수신하여 서버로 저장한다.
def sendWeight(request):
    # POST 요청일 경우에는 파일 수신, GET 요청이면 업로드 폼 반환
    if request.method == 'POST':
            form = WeightFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse(JsonResponse({'success': 'upload complete'}), status=202)
            else:
                return HttpResponse(JsonResponse({'Fail': 'unvalid form'}), status=412)
    else:
        form = WeightFileForm()
        return render(request, 'upload.html', {'form': form})

# Weight 파일 리스트에서 반환한 파일의 id 값을 받아 파일 다운로드 기능 제공
def downloadWeight(request, file_id):
    # GET 요청일 경우에만 응답
    if request.method == 'GET':
        db.reset_queries()
        weightFiles = WeightFile.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, weightFiles.weight_file.path)
        filename = os.path.basename(file_path)
        # 파일을 한번에 전송하는것은 부하가 커지므로 8192 바이트 단위로 끊어 스트림 방식으로 전송한다
        chunk_size = 8192
        if os.path.exists(file_path):
            # Response 헤더에 전송 타입, 파일의 크기, 보내는 파일의 이름을 설정해 응답한다.
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

# 현재 등록되어 사용 가능한 Image 파일 리스트를 Json으로 응답
def getImageList(request):
    # GET 요청일 경우에만 생성일의 내림차순으로 정렬한 list를 가져온다
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

# Image 파일 리스트에서 반환한 파일의 id 값을 받아 파일 다운로드 기능 제공
def downloadImage(request, file_id):
    if request.method == 'GET':
        db.reset_queries()
        imageFiles = ImageFile.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, imageFiles.image_file.path)
        filename = os.path.basename(file_path)
        # 파일을 한번에 전송하는것은 부하가 커지므로 8192 바이트 단위로 끊어 스트림 방식으로 전송한다
        chunk_size = 8192
        if os.path.exists(file_path):
            # Response 헤더에 전송 타입, 파일의 크기, 보내는 파일의 이름을 설정해 응답한다.
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

# Image 파일을 수신하여 서버로 저장한다.
def sendImage(request):
    # POST 요청일 경우에는 파일 수신, GET 요청이면 업로드 폼 반환
    if request.method == 'POST':
            form = ImageFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse(JsonResponse({'success': 'upload complete'}), status=202)
            else:
                return HttpResponse(JsonResponse({'Fail': 'unvalid form'}), status=412)
    else:
        form = ImageFileForm()
        return render(request, 'upload.html', {'form': form})