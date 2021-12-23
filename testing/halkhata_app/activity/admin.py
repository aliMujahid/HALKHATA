from typing import ClassVar
from django.contrib import admin


from .models import  Ride, Run, Walk, Activity, Exercise

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['date',]

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ['name' ,'date', 'distance']

@admin.register(Run)
class RideAdmin(admin.ModelAdmin):
    list_display = ['name' ,'date', 'distance']

@admin.register(Walk)
class RideAdmin(admin.ModelAdmin):
    list_display = ['name' ,'date', 'distance']

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'deficulty_level']
    prepopulated_fields = {'slug':('name',)}
    actions = ['set_muscle_group']