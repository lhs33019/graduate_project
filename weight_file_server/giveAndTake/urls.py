from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('blank/', views.blank, name="blank"),
    path('buttons/', views.buttons, name="buttons"),
    path('cards/', views.cards, name="cards"),
    path('charts/', views.charts, name="charts"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('login/', views.login, name="login"),
    path('posting/', views.posting, name="posting"),
    path('register/', views.register, name="register"),
    path('tables/', views.tables, name="tables"),
    path('utilities_animation/', views.utilities_animation, name="utilities_animation"),
    path('utilities_border/', views.utilities_border, name="utilities_border"),
    path('utilities_color/', views.utilities_color, name="utilities_color"),
    path('utilities_other/', views.utilities_other, name="utilities_other"),
    path('logout/', views.logout, name="logout"),
    path('get404/', views.get404, name="get404"),
]