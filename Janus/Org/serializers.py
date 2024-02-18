"""
Serializers for Worker APIS
"""
from rest_framework import serializers

from core.models import (
    company,
    businessUnit,
    department,
    location,
    costCenter,
    title,
)


class companySerializer(serializers.ModelSerializer):
    """Serializer for Company."""

    class Meta:
        model = company
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates

class businessUnitSerializer(serializers.ModelSerializer):
    """Serializer for businessUnits."""

    class Meta:
        model = businessUnit
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class departmentSerializer(serializers.ModelSerializer):
    """Serializer for departments."""

    class Meta:
        model = department
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class locationSerializer(serializers.ModelSerializer):
    """Serializer for location."""

    class Meta:
        model = location
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class costCenterSerializer(serializers.ModelSerializer):
    """Serializer for costCenter."""

    class Meta:
        model = costCenter
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class titleSerializer(serializers.ModelSerializer):
    """Serializer for Titles."""

    class Meta:
        model = title
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates