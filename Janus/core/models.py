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