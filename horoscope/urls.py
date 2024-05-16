from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('info_by_date/', views.redirect_form),
    path('<int:month>/<int:day>/', views.get_info_by_date),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
    ]