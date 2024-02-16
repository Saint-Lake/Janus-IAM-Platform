"""
Serializers for Worker APIS
"""
from rest_framework import serializers

from core.models import (
    Workers,
    companies,
    businessUnits,
    departments,
    locations,
    costCenters,
    titles,
)


class CommonCodeListFieldsSerializer(serializers.ModelSerializer):
    """Serializer for Common Code List Fields."""

    class Meta:
        abstract = True
        fields = ['codeValue']

    def to_internal_value(self, data):
        # Custom logic to convert incoming data to internal value
        if isinstance(data, dict):
            code_value = data.get('codeValue')
            if code_value:
                existing_instance = self.Meta.model.objects.filter(codeValue=code_value).first()
                if existing_instance:
                    # If an existing instance is found, return that instance
                    return existing_instance
                else:
                    raise serializers.ValidationError(f"{self.Meta.model.__name__} with codeValue '{code_value}' does not exist.")
            else:
                raise serializers.ValidationError(f"Invalid {self.Meta.model.__name__} data [No CodeValue provided]")

        return super().to_internal_value(data)


class workercompanySerializer(CommonCodeListFieldsSerializer):
    """Serializer for Company."""

    class Meta:
        model = companies
        fields = CommonCodeListFieldsSerializer.Meta.fields
        partial = True  # Added this line to allow partial updates


class workerbusinessUnitSerializer(CommonCodeListFieldsSerializer):
    """Serializer for Business Unit."""

    class Meta:
        model = businessUnits
        fields = CommonCodeListFieldsSerializer.Meta.fields
        partial = True  # Added this line to allow partial updates


class workerdepartmentSerializer(CommonCodeListFieldsSerializer):
    """Serializer for Business Unit."""

    class Meta:
        model = departments
        fields = CommonCodeListFieldsSerializer.Meta.fields
        partial = True  # Added this line to allow partial updates


class workerlocationSerializer(CommonCodeListFieldsSerializer):
    """Serializer for Business Unit."""

    class Meta:
        model = locations
        fields = CommonCodeListFieldsSerializer.Meta.fields
        partial = True  # Added this line to allow partial updates


class workercostCenterSerializer(CommonCodeListFieldsSerializer):
    """Serializer for Business Unit."""

    class Meta:
        model = costCenters
        fields = CommonCodeListFieldsSerializer.Meta.fields
        partial = True  # Added this line to allow partial updates


class workertitleSerializer(CommonCodeListFieldsSerializer):
    """Serializer for Business Unit."""

    class Meta:
        model = titles
        fields = CommonCodeListFieldsSerializer.Meta.fields
        partial = True  # Added this line to allow partial updates


class WorkerSerializer(serializers.ModelSerializer):
    """Serializer for Worker"""
    
    company = workercompanySerializer(many=False, required=True)
    businessUnit = workerbusinessUnitSerializer(many=False, required=True)
    department = workerdepartmentSerializer(many=False, required=True)
    location = workerlocationSerializer(many=False, required=True)
    costCenter = workercostCenterSerializer(many=False, required=True)
    title = workertitleSerializer(many=False, required=True)

    class Meta:
        model = Workers
        fields = [
            'associateOID',
            'WorkerId',
            'workerStatus',
            'prefered_name',
            'prefered_lastName',
            'company',
            'businessUnit',
            'department',
            'location',
            'costCenter',
            'title',
        ]

    def _get_or_create_common_code_list(self, serializer_class, instance, data):
        # Helper method to get or create instances of CommonCodeListFields models
        serializer = serializer_class(instance=instance, data=data)
        if serializer.is_valid():
            return serializer.save()
        else:
            raise serializers.ValidationError(f"Invalid {serializer_class.Meta.model.__name__} data: {serializer.errors}")

    def create(self, validated_data):
        # Create method for WorkerSerializer
        company_data = validated_data.pop('company', None)
        business_unit_data = validated_data.pop('businessUnit', None)
        department_data = validated_data.pop('department', None)
        location_data = validated_data.pop('location', None)
        costCenter_data = validated_data.pop('costCenter', None)
        title_data = validated_data.pop('title', None)

        if company_data:
            # Check if company_data is an instance of the model
            if isinstance(company_data, companies):
                # if so this instance = the data we need
                validated_data['company'] = company_data
            else:
                # else lets see if we can find it
                validated_data['company'] = self._get_or_create_common_code_list(workercompanySerializer, None, company_data)

        if business_unit_data:
            # Check if business_unit_data is an instance of the model
            if isinstance(business_unit_data, businessUnits):
                # if so this instance = the data we need
                validated_data['businessUnit'] = business_unit_data
            else:
                # else lets see if we can find it
                validated_data['businessUnit'] = self._get_or_create_common_code_list(workerbusinessUnitSerializer, None, business_unit_data)

        if department_data:
            # Check if department_data is an instance of the model
            if isinstance(department_data, departments):
                # if so this instance = the data we need
                validated_data['department'] = department_data
            else:
                # else lets see if we can find it
                validated_data['department'] = self._get_or_create_common_code_list(workerdepartmentSerializer, None, department_data)

        if location_data:
            # Check if location_data is an instance of the model
            if isinstance(location_data, locations):
                # if so this instance = the data we need
                validated_data['location'] = location_data
            else:
                # else lets see if we can find it
                validated_data['location'] = self._get_or_create_common_code_list(workerlocationSerializer, None, location_data)

        if costCenter_data:
            # Check if costCenter_data is an instance of the model
            if isinstance(costCenter_data, costCenters):
                # if so this instance = the data we need
                validated_data['costCenter'] = costCenter_data
            else:
                # else lets see if we can find it
                validated_data['costCenter'] = self._get_or_create_common_code_list(workercostCenterSerializer, None, costCenter_data)

        if title_data:
            # Check if title_data is an instance of the model
            if isinstance(title_data, titles):
                # if so this instance = the data we need
                validated_data['title'] = title_data
            else:
                # else lets see if we can find it
                validated_data['title'] = self._get_or_create_common_code_list(workertitleSerializer, None, title_data)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Update method for WorkerSerializer
        company_data = validated_data.pop('company', None)
        business_unit_data = validated_data.pop('businessUnit', None)
        department_data = validated_data.pop('department', None)
        location_data = validated_data.pop('location', None)
        costCenter_data = validated_data.pop('costCenter', None)
        title_data = validated_data.pop('title', None)

        if company_data:
            # Check if company_data is an instance of the model
            if isinstance(company_data, companies):
                # if so this instance = the data we need
                instance.company = company_data
            else:
                # else lets see if we can find it
                instance.company = self._get_or_create_common_code_list(
                    workercompanySerializer, instance.company, company_data
                )

        if business_unit_data:
            # Check if business_unit_data is an instance of the model
            if isinstance(business_unit_data, businessUnits):
                # if so this instance = the data we need
                instance.businessUnit = business_unit_data
            else:
                # else lets see if we can find it
                instance.businessUnit = self._get_or_create_common_code_list(
                    workerbusinessUnitSerializer, instance.businessUnit, business_unit_data
                )

        if department_data:
            # Check if department_data is an instance of the model
            if isinstance(department_data, departments):
                # if so this instance = the data we need
                instance.department = department_data
            else:
                # else lets see if we can find it
                instance.department = self._get_or_create_common_code_list(
                    workerdepartmentSerializer, instance.department, department_data
                )

        if location_data:
            # Check if location_data is an instance of the model
            if isinstance(location_data, locations):
                # if so this instance = the data we need
                instance.location = location_data
            else:
                # else lets see if we can find it
                instance.location = self._get_or_create_common_code_list(
                    workerlocationSerializer, instance.location, location_data
                )

        if costCenter_data:
            # Check if costCenter_data is an instance of the model
            if isinstance(costCenter_data, costCenters):
                # if so this instance = the data we need
                instance.costCenter = costCenter_data
            else:
                # else lets see if we can find it
                instance.costCenter = self._get_or_create_common_code_list(
                    workercostCenterSerializer, instance.costCenter, costCenter_data
                )

        if title_data:
            # Check if title_data is an instance of the model
            if isinstance(title_data, titles):
                # if so this instance = the data we need
                instance.title = title_data
            else:
                # else lets see if we can find it
                instance.title = self._get_or_create_common_code_list(
                    workertitleSerializer, instance.title, title_data
                )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class WorkerDetailSerializer(WorkerSerializer):
    class Meta(WorkerSerializer.Meta):
        fields = WorkerSerializer.Meta.fields + ['firstName', 'lastName']