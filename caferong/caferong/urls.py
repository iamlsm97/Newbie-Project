"""caferong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.http import HttpResponseRedirect
from basic.views import home, loadinfo, loadlist, loadmap, new_cafe, edit_cafe, delete_cafe, loadtest
from basic.models import Cafe

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda r: HttpResponseRedirect('/home/')),
    url(r'^home/', home),
    url(r'^map_info/', loadinfo),
    url(r'^cafe_list/', loadlist),
    url(r'^cafe_map/', loadmap),
    url(r'^new_cafe/$', new_cafe),
    url(r'^edit_cafe/([^/]+)/$', edit_cafe),
    url(r'^delete_cafe/([^/]+)/$', delete_cafe),
    url(r'^test/', loadtest),
]
