from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    # api 3개 - 저장된 파일 리스트로 출력, POST로 s3에 파일 올리기, GET으로 파일 다운로드받기
    path('weight/list/', views.getWeightList, name="weightFile_list"),
    path('weight/send/', views.sendWeight, name="weightFile_send"),
    path('weight/download/<int:file_id>/', views.downloadWeight, name="weightFile_download"),
    path('image/list/', views.getImageList, name="imageFile_list"),
    path('image/send/', views.sendImage, name="imageFile_send"),
    path('image/download/<int:file_id>/', views.downloadImage, name="imageFile_download"),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)