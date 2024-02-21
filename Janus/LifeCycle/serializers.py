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
        fields = ['life_event_id', 'event_status', 'event_type', 'start_date', 'migration_window', 'end_date']
        read_only_fields = ['life_event_id', 'end_date']

class LifeCycleCaseSerializer(serializers.ModelSerializer):
    Worker = RelatedWorkerSerializer(required=True)
    Event = LifeCycleEventSerializer(many=True, required=False)

    class Meta:
        model = lifeCycleCase
        fields = ['life_cycle_id', 'case_status', 'Worker', 'Event']
        read_only_fields = ['life_cycle_id']

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

        # Update or create the related 'Event' instances if provided in the request
        events_data = validated_data.get('Event', [])
        for event_data in events_data:
            event_id = event_data.get('life_event_id', None)
            if event_id:
                # If event_id is present, update the existing event
                event_instance = lifeCycleEvent.objects.get(pk=event_id, lifeCycleCase=instance)
                for key, value in event_data.items():
                    setattr(event_instance, key, value)
                event_instance.save()
            else:
                # If event_id is not present, create a new event
                lifeCycleEvent.objects.create(lifeCycleCase=instance, **event_data)

        return instance

class LifeCycleCaseDetailSerializer(LifeCycleCaseSerializer):
    class Meta(LifeCycleCaseSerializer.Meta):
        fields = LifeCycleCaseSerializer.Meta.fields
