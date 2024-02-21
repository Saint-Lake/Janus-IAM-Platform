"""
Views for the LifeCycle APIS.
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
    lifeCycleEvent,
    lifeCycleCase
)
from LifeCycle import serializers


class lifeCycleEventViewSet(viewsets.ModelViewSet):
    """Viewset for Workers APIs."""
    serializer_class = serializers.LifeCycleEventSerializer
    queryset = lifeCycleEvent.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve workers for authenticated users."""
        queryset = self.queryset

        return queryset.order_by('life_event_id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.LifeCycleEventSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new Worker"""
        serializer.save()


class lifeCycleCaseViewSet(viewsets.ModelViewSet):
    """Viewset for Workers APIs."""
    serializer_class = serializers.LifeCycleCaseDetailSerializer
    queryset = lifeCycleCase.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve workers for authenticated users."""
        queryset = self.queryset

        return queryset.order_by('life_cycle_id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.LifeCycleCaseSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new Worker"""
        serializer.save()