"""
Serializers for Worker APIS
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
        partial = True  # Added this line to allow partial updates
    
    def to_internal_value(self, data):
        if isinstance(data, dict):
            # Check if a company with the same codeValue already exists
            code_value = data.get('codeValue')
            # if code_value is not None
            if code_value:
                # Query the database for an existing company with the same codeValue
                existing_company = companies.objects.filter(codeValue=code_value).first()
                # If an existing company is found, return that instance
                if existing_company:
                    # If an existing company is found, return that instance
                    return existing_company
        # If no existing company is found, fall back to the default behavior
        return super().to_internal_value(data)

class WorkerSerializer(serializers.ModelSerializer):
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

    def _get_or_create_company(self, company_data, worker_instance):
        company_serializer = companySerializer(worker_instance.company, data=company_data)
        if company_serializer.is_valid():
            return companies.objects.get_or_create(**company_serializer.validated_data)[0]
        else:
            raise serializers.ValidationError("Invalid company data")

    def create(self, validated_data):
        company_data = validated_data.pop('company', None)
        if company_data:
            # If company_data is an instance of companies, use it directly
            if isinstance(company_data, companies):
                company_obj = company_data
            else:
                company_serializer = companySerializer(data=company_data)
                if company_serializer.is_valid():
                    company_obj, created = companies.objects.get_or_create(**company_serializer.validated_data)
                else:
                    raise serializers.ValidationError("Invalid company data")
            validated_data['company'] = company_obj
        else:
            raise serializers.ValidationError("Company data is required.")

        return super().create(validated_data)

    def update(self, instance, validated_data):
        company_data = validated_data.pop('company', None)

        if company_data:
            # If company_data is an instance of companies, use it directly
            if isinstance(company_data, companies):
                instance.company = company_data
            else:
                # Update or create the Company instance
                company_serializer = companySerializer(instance.company, data=company_data)
                if company_serializer.is_valid():
                    # Get or create the Company instance
                    company_obj, created = companies.objects.get_or_create(**company_serializer.validated_data)
                    instance.company = company_obj
                else:
                    # Handle the case when company data is not valid
                    raise serializers.ValidationError("Invalid company data")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class WorkerDetailSerializer(WorkerSerializer):
    class Meta(WorkerSerializer.Meta):
        fields = WorkerSerializer.Meta.fields + ['firstName', 'lastName']