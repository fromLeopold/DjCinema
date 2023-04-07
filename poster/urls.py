from django.urls import path
from poster.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', welcome, name='welcome'),
    path('djcinema/', about_cinema, name='dj_cinema'),
    path('djcinema/afisha', afisha, name='afisha'),
    path('djcinema/afisha/<int:film_id>/', about_film, name='film_about'),
    path('djcinema/news', news, name='news'),
    path('djcinema/<int:new_id>/', about_new, name='new_about'),
    path('djcinema/review', review, name='review'),
    path('registration/', registration, name='registration'),
    path('login/', site_login, name='login'),
    path('site_logout/', site_logout, name='site_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
