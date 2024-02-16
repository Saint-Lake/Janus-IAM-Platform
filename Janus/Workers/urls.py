"""
URL mappings for Workers app
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from Workers import views


router = DefaultRouter()
router.register('workers', views.WorkerViewSet)

app_name = 'Workers'

urlpatterns = [
    path('', include(router.urls)),
]