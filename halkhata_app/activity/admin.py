from django.contrib import admin

from .models import Activity, ActivityType, Ride

admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(Ride)
