"""
Views for the Workers APIS.
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
    Worker
)
from Workers import serializers


class WorkerViewSet(viewsets.ModelViewSet):
    """Viewset for Workers APIs."""
    serializer_class = serializers.WorkerDetailSerializer
    queryset = Worker.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve workers for authenticated users."""
        queryset = self.queryset

        return queryset.order_by('prefered_lastName')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.WorkerSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new Worker"""
        serializer.save()
