from django.contrib import admin
from django.urls import path , include
import giveAndTake.views, fileManage.views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    # 관리자 페이지 제공
    path('admin/', admin.site.urls),
    # 일반적인 웹 페이지 제공
    path('image/', include('giveAndTake.urls')),
    path('', giveAndTake.views.index, name="home"),
    # 파일과 관련된 api 라우팅
    path('file/', include('fileManage.urls')),
    # 파일 다이렉트 다운로드 링크 제공
    path('media/<path:path>/', fileManage.views.download_direct),
    # api 문서 제공
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
]
handler404 = 'giveAndTake.views.handler404'