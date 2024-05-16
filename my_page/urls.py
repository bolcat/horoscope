from django.urls import path, include
urlpatterns = [
    # path('horoscope/', include('horoscope.urls')),
    path('', include('horoscope.urls')),
    ]