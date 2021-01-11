from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart, petschart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('post/<str:slug>/', showpost),
    path('petschart/', petschart),
    path('', homepage),
]
