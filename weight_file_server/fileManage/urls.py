from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    ##필요한 api 3개 - 저장된 파일 리스트로 출력, POST로 s3에 파일 올리기, GET으로 s3 파일 다운로드받기
    path('list/', views.getlist, name="file_list"),
    path('send/', views.send, name="file_send"),
    path('download/<int:file_id>/', views.download, name="file_download"),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)