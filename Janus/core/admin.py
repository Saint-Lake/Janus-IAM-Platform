"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models



admin.site.register(models.Worker)
admin.site.register(models.lifeCycleEvent)
admin.site.register(models.lifeCycleCase)
admin.site.register(models.company)
admin.site.register(models.businessUnit)
admin.site.register(models.department)
admin.site.register(models.location)
admin.site.register(models.costCenter)
admin.site.register(models.title)
