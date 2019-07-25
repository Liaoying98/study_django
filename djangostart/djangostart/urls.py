"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
# 自定义需要导包
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 自定义路由
    url(r'^demo/$', views.demo),
    url(r'^demo01/$', views.demo01),
    url(r'^demo02_form/$', views.demo02_form),
    url(r'^demo02_form2/$', views.demo02_form2),
    url(r'^demo02_form3/$', views.demo02_form3),
    url(r'^demo02_form_db/$', views.demo02_form_db),
    url(r'^login/$', views.login),
]
