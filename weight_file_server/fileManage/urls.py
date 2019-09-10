from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from .views import *
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'image', ImageFileViewSet)
router.register(r'weight', WeightFileViewSet)

urlpatterns = [
    ##필요한 api 3개 - 저장된 파일 리스트로 출력, POST로 s3에 파일 올리기, GET으로 파일 다운로드받기
    path('weight/', views.getWeightList, name="weightFile_list"),
    path('weight/send/', views.sendWeight, name="weightFile_send"),
    path('weight/download/<int:file_id>/', views.downloadWeight, name="weightFile_download"),
    path('weight/<int:file_id>/', views.downloadWeight, name="weightFile_download"),
    path('image/', views.getImageList, name="imageFile_list"),
    path('image/send/', views.sendImage, name="imageFile_send"),
    path('image/download/<int:file_id>/', views.downloadImage, name="imageFile_download"),
    path('image/<int:file_id>/', views.downloadImage, name="imageFile_download"),
    url(r'^', include(router.urls)),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)