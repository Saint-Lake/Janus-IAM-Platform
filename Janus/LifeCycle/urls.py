"""
URL mappings for LifeCycle app
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from LifeCycle import views


router = DefaultRouter()
router.register('LifeCycleCase', views.lifeCycleCaseViewSet)
router.register('LifeCycleEvent', views.lifeCycleEventViewSet)

app_name = 'LifeCycle'

urlpatterns = [
    path('', include(router.urls)),
]