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


class companies(CommonCodeListFields):
    """Company codelist Model"""
    pass


class businessUnits(CommonCodeListFields):
    """BU codelist Model"""
    pass


class departments(CommonCodeListFields):
    """Departments codelist Model"""
    pass


class locations(CommonCodeListFields):
    """locations codelist Model"""
    pass


class costCenters(CommonCodeListFields):
    """Cost Centers codelist Model"""
    pass


class titles(CommonCodeListFields):
    """Jobs codelist Model"""
    pass
    

class Workers(models.Model):
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
    company = models.ForeignKey(
        companies,
        on_delete=models.CASCADE,
    )
    businessUnit = models.ForeignKey(
        businessUnits,
        on_delete=models.CASCADE,
    )
    department = models.ForeignKey(
        departments,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    location = models.ForeignKey(
        locations,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    costCenter = models.ForeignKey(
        costCenters,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.ForeignKey(
        titles,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.WorkerId