"""
URL mappings for Org app
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from Org import views


router = DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('businessUnits', views.BusinessUnitViewSet)
router.register('departments', views.DeparmentViewSet)
router.register('locations', views.LocationViewSet)
router.register('costCenters', views.CostCenterViewSet)
router.register('titles', views.TitleViewSet)

app_name = 'Org'

urlpatterns = [
    path('', include(router.urls)),
]