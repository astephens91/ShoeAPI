"""shoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include

from rest_framework import routers

from shoes import views
from shoes.models import ShoeColor, ShoeType, Shoe, Manfacturer

router = routers.DefaultRouter()
router.register(r'shoe', views.ShoeView)
router.register(r'shoetype', views.ShoeTypeView)
router.register(r'shoecolor', views.ShoeColorView)
router.register(r'manufacturer', views.ManufacturerView)

admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoe)
admin.site.register(Manufacturer)



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
