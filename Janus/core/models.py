"""
Database models.
"""
import uuid
import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class CommonCodeListFields(models.Model):
    """Common codelist Model"""
    codeValue = models.CharField(max_length=55, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.CharField(max_length=255)


class company(CommonCodeListFields):
    """Company codelist Model"""
    pass


class businessUnit(CommonCodeListFields):
    """BU codelist Model"""
    pass


class department(CommonCodeListFields):
    """Departments codelist Model"""
    pass


class location(CommonCodeListFields):
    """locations codelist Model"""
    pass


class costCenter(CommonCodeListFields):
    """Cost Centers codelist Model"""
    pass


class title(CommonCodeListFields):
    """Jobs codelist Model"""
    pass
    

class Worker(models.Model):
    associateOID = models.CharField(max_length=55)
    WorkerId = models.CharField(max_length=55, primary_key=True)
    workerStatus = models.CharField(
        max_length=10,
        choices = (
            ("Active","Active"),
            ("Terminated","Terminated"),
            ("Leave","Leave"),
        )
    )
    prefered_name = models.CharField(max_length=55)
    prefered_lastName = models.CharField(max_length=55)
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    startDate = models.DateTimeField(null=True)
    TermDate = models.DateTimeField(null=True, blank=True)
    company = models.ForeignKey(
        company,
        on_delete=models.CASCADE,
    )
    businessUnit = models.ForeignKey(
        businessUnit,
        on_delete=models.CASCADE,
    )
    department = models.ForeignKey(
        department,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    location = models.ForeignKey(
        location,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    costCenter = models.ForeignKey(
        costCenter,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.ForeignKey(
        title,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.WorkerId

class lifeCycleEvent(models.Model):
    life_event_id = models.CharField(max_length=11, primary_key=True, editable=False)
    event_status = models.CharField(
        max_length=10,
        choices = (
            ("Active","Active"),
            ("Complete","Complete"),
        )
    )
    event_type = models.CharField(
        max_length=10,
        choices = (
            ("Onboard","Onboard"),
            ("Offboard","Offboard"),
            ("Promotion","Promotion"),
            ("Transfer","Transfer"),
        )
    )
    start_date = models.DateTimeField()
    migration_window = models.IntegerField()
    end_date = models.DateTimeField(editable=False)


    def save(self, *args, **kwargs):
        # Generate and set the primary key before saving
        if not self.life_cycle_id:
            last_id = lifeCycleEvent.objects.order_by('-life_cycle_id').first()
            if last_id:
                last_number = int(last_id.life_cycle_id.split('-')[1])
                new_number = last_number + 1
            else:
                new_number = 1
            self.life_cycle_id = f'EVENT-{new_number:05d}'

            # Calculate end date based on start date and migration window
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.migration_window)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.life_cycle_id

class lifeCycleCase(models.Model):
    # Custom primary key CharField
    life_cycle_id = models.CharField(max_length=10, primary_key=True, editable=False)
    case_status = models.CharField(
        max_length=15,
        choices = (
            ("Onboarding","Onboarding"),
            ("Hired","Hired"),
            ("Moving","Moving"),
            ("Leaving","Leaving"),
            ("Rehiring","Rehiring"),
            ("Archived","Archived"),
        )
    )
    Worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
    )
    Event = models.ManyToManyField(lifeCycleEvent, blank=True)

    def save(self, *args, **kwargs):
        # Generate and set the primary key before saving
        if not self.life_cycle_id:
            last_id = lifeCycleCase.objects.order_by('-life_cycle_id').first()
            if last_id:
                last_number = int(last_id.life_cycle_id.split('-')[1])
                new_number = last_number + 1
            else:
                new_number = 1
            self.life_cycle_id = f'LIFE-{new_number:05d}'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.life_cycle_id