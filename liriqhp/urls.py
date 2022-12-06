"""liriqhp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iphone.views import iphone
from oppo.views import oppo
from realme.views import realme
from samsung.views import samsung
from xiaomi.views import xiaomi
from liriqhp.views import liriqhp
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iphone/', iphone),
    path('oppo/', oppo),
    path('realme/', realme),
    path('samsung/', samsung),
    path('xiaomi/', xiaomi),
    path('liriqhp/', liriqhp),
    path('', views.liriqhp),
]
