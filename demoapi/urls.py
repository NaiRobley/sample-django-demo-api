"""demo_api URL Configuration

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
from django.conf.urls import url
from demoapi import views
#from rest_framework import routers
#from .views import StudentViewSet, UniversityViewSet, home

# router = routers.DefaultRouter()
# router.register(r'students', StudentViewSet)
# router.register(r'universities', UniversityViewSet)
# # router.register(r'^home', views.home)
#
#
# urlpatterns = router.urls

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^students/(?P<id>[0-9]+)$', views.student, name='students'),
    url(r'^university/(?P<id>[0-9]+)/$', views.university, name='university'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    # 'api.views',
]
