"""
Serializers for Worker APIS
"""
from rest_framework import serializers

from core.models import (
    companies,
    businessUnits,
    departments,
    locations,
    costCenters,
    titles,
)


class companySerializer(serializers.ModelSerializer):
    """Serializer for Company."""

    class Meta:
        model = companies
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates

class businessUnitSerializer(serializers.ModelSerializer):
    """Serializer for businessUnits."""

    class Meta:
        model = businessUnits
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class departmentSerializer(serializers.ModelSerializer):
    """Serializer for departments."""

    class Meta:
        model = departments
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class locationSerializer(serializers.ModelSerializer):
    """Serializer for location."""

    class Meta:
        model = locations
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class costCenterSerializer(serializers.ModelSerializer):
    """Serializer for costCenter."""

    class Meta:
        model = costCenters
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates


class titleSerializer(serializers.ModelSerializer):
    """Serializer for Titles."""

    class Meta:
        model = titles
        fields = ['codeValue', 'name', 'description', 'owner']
        partial = True  # Added this line to allow partial updates