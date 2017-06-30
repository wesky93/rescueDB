"""rescueDB URL Configuration

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

from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from record.views import *

urlpatterns = [
    # 메인 페이지
    url(r'^$',Home.as_view(),name='home'),
    # 구조 기록
    url(r'^list/$',login_required( Records.as_view() ),name='list'),
    # 상세 구조 페이지
    url(r'detail/(?P<pk>\d+)/$',login_required(Detail.as_view()),name='detail'),
    # 구조 정보 입력 폼
    url(r'^input/$',login_required(Input.as_view()),name='input'),
]