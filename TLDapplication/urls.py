"""TLDapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users import views
from TLD import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^tableview/', views.tableview, name='tableview'),
    url(r'^chartview/', views.chartview, name='chartview'),
    url(r'^dataprocess/', views.dataprocess, name='dataprocess'),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
]
