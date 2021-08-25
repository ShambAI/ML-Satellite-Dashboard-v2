# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import RemOrganization, RemRole, RemUser, Nursery, NurseryPlantsHistory, MotherTree, Plantation, YieldHistory

admin.site.register(RemOrganization)
admin.site.register(RemRole)
admin.site.register(RemUser)
admin.site.register(Nursery)
admin.site.register(NurseryPlantsHistory)
admin.site.register(MotherTree)
admin.site.register(Plantation)
admin.site.register(YieldHistory)
