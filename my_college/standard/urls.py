from django.urls import path,include
from django.contrib import admin
from standard.views import SectionViewSet,StudentViewSet
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'students',StudentViewSet)

urlpatterns = [
    path('',include(router.urls))
]