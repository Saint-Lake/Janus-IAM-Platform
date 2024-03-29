"""
Views for the Org APIS.
"""
from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    company,
    businessUnit,
    department,
    location,
    costCenter,
    title,
)
from Org import serializers


class BaseCodeListAttrViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """Base viewset for Org attributes."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CompanyViewSet(BaseCodeListAttrViewSet):
    """Manage Companies in the database."""
    serializer_class = serializers.companySerializer
    queryset = company.objects.all()


class BusinessUnitViewSet(BaseCodeListAttrViewSet):
    """Manage Business Units in the database."""
    serializer_class = serializers.businessUnitSerializer
    queryset = businessUnit.objects.all()


class DeparmentViewSet(BaseCodeListAttrViewSet):
    """Manage Departments in the database."""
    serializer_class = serializers.departmentSerializer
    queryset = department.objects.all()


class LocationViewSet(BaseCodeListAttrViewSet):
    """Manage Locations in the database."""
    serializer_class = serializers.locationSerializer
    queryset = location.objects.all()


class CostCenterViewSet(BaseCodeListAttrViewSet):
    """Manage Cost Centers in the database."""
    serializer_class = serializers.costCenterSerializer
    queryset = costCenter.objects.all()


class TitleViewSet(BaseCodeListAttrViewSet):
    """Manage Titles in the database."""
    serializer_class = serializers.titleSerializer
    queryset = title.objects.all()