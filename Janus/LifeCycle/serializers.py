"""
Serializers for Worker APIS
"""
from rest_framework import serializers

from core.models import (
    lifeCycleEvent,
    lifeCycleCase,
    Worker
)


class RelatedWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['WorkerId']
    
    def to_internal_value(self, data):
        if isinstance(data, Worker):
            return data
        worker_id = data.get('WorkerId')
        # Assume that the Worker with the specified WorkerId already exists
        try:
            return Worker.objects.get(WorkerId=worker_id)
        except Worker.DoesNotExist:
            raise serializers.ValidationError("Worker with this WorkerId does not exist.")

class LifeCycleEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = lifeCycleEvent
        fields = '__all__'

class LifeCycleCaseSerializer(serializers.ModelSerializer):
    Worker = RelatedWorkerSerializer(required=True)
    related_events = serializers.SerializerMethodField()

    class Meta:
        model = lifeCycleCase
        fields = ['life_cycle_id', 'case_status', 'Worker', 'related_events']
        read_only_fields = ['life_cycle_id','related_events']

    def get_related_events(self, instance):
        # Assuming the related_name for the ForeignKey in lifeCycleEvent is 'case'
        events = lifeCycleEvent.objects.filter(case_id=instance)
        serialized_events = LifeCycleEventSerializer(events, many=True).data
        return serialized_events

    def create(self, validated_data):
        worker_data = validated_data.pop('Worker', {})
        
        # Check if worker_data is an instance of Worker
        if isinstance(worker_data, Worker):
            worker_instance = worker_data
        else:
            worker_id = worker_data.get('WorkerId')
            # Assume that the Worker with the specified WorkerId already exists
            try:
                worker_instance = Worker.objects.get(WorkerId=worker_id)
            except Worker.DoesNotExist:
                raise serializers.ValidationError({"Worker": ["Worker with the specified WorkerId does not exist."]})

        # Create the LifeCycleCase instance without creating a new worker
        instance = lifeCycleCase.objects.create(Worker=worker_instance, **validated_data)

        return instance

    def update(self, instance, validated_data):
        # Update lifeCycleCase instance
        instance.case_status = validated_data.get('case_status', instance.case_status)
        instance.save()

        # Validate and associate with existing or raise error if not found
        worker_data = validated_data.get('Worker', {})
        if worker_data:
            if isinstance(worker_data, Worker):
                worker_instance = worker_data
            else:
                worker_id = worker_data.get('WorkerId')
                # Assume that the Worker with the specified WorkerId already exists
                try:
                    worker_instance = Worker.objects.get(WorkerId=worker_id)
                except Worker.DoesNotExist:
                    raise serializers.ValidationError({"Worker": ["Worker with the specified WorkerId does not exist."]})

            instance.Worker = worker_instance

        return instance

class LifeCycleCaseDetailSerializer(LifeCycleCaseSerializer):
    class Meta(LifeCycleCaseSerializer.Meta):
        fields = LifeCycleCaseSerializer.Meta.fields
