"""
Serializers for Recipe APIS
"""
from rest_framework import serializers

from core.models import (
    Workers,
    companies,
)


class companySerializer(serializers.ModelSerializer):
    """Serializer for Company."""

    class Meta:
        model = companies
        fields = ['codeValue', 'name', 'description', 'owner']

class WorkerSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    company = companySerializer(many=False, required=True)
    
    class Meta:
        model = Workers
        fields = [
            'associateOID',
            'WorkerId',
            'workerStatus',
            'prefered_name',
            'prefered_lastName',
            'company',
        ]

    def _get_or_create_company(self, company, Worker):
        """Handle getting or creating Companys as needed."""
        print(company, Worker)
        company_obj, created = companies.objects.get_or_create(
            **company,
        )
        print(company_obj, created)
        Worker.company.add(company_obj)

    def create(self, validated_data):
        """Create a recipe."""
        company = validated_data.pop('company', [])
        Worker = Workers.objects.create(**validated_data)
        self._get_or_create_company(company, Worker)

        return Worker

    def update(self, instance, validated_data):
        """Update recipe."""
        company = validated_data.pop('company', [])
        print(company)
        if company is not None:
            instance.company.clear()
            self._get_or_create_company(company, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class WorkerDetailSerializer(WorkerSerializer):
    """Serializer for recipe detail view."""

    class Meta(WorkerSerializer.Meta):
        fields = WorkerSerializer.Meta.fields + ['firstName', 'lastName']