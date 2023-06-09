from django.contrib import admin
from django.urls import path, include

from poster.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('poster.urls'))
]

handler404 = pageNotFound
