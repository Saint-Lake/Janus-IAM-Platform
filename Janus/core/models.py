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


class companies(models.Model):
    """Company codelist Model"""
    codeValue = models.CharField(max_length=55, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.CharField(max_length=255)
    

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

    def __str__(self):
        return self.WorkerId