from django.contrib.admin.decorators import register
from django.db import models
from django.db.models.fields import TimeField
from django.urls import reverse
import datetime


class Activity(models.Model):
    """A days all activitys"""
    date = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ('-date',)
        verbose_name_plural  = 'activities'





class Ride(models.Model):
    type = 'ride'
    activity = models.ForeignKey(Activity, related_name='rides', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()
    elev_gain = models.IntegerField()
    avg_speed = models.DecimalField(max_digits=6, decimal_places=2)
    cal_burned = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return "Ride"

    def get_absolute_url(self):
        return reverse('activity:activity_details', args=[self.type, self.id])


#test models.
class Run(models.Model):
    type = 'run'
    activity = models.ForeignKey(Activity, related_name='runs', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()
    elev_gain = models.IntegerField()
    avg_speed = models.DecimalField(max_digits=6, decimal_places=2)
    cal_burned = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return "Run"

    def get_absolute_url(self):
        return reverse('activity:activity_details', args=[self.type, self.id])



class Walk(models.Model):
    type = 'walk'
    activity = models.ForeignKey(Activity, related_name='walks', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()
    elev_gain = models.IntegerField()
    avg_speed = models.DecimalField(max_digits=6, decimal_places=2)
    cal_burned = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return "Walk"

    def get_absolute_url(self):
        return reverse('activity:activity_details', args=[self.type, self.id])


class Exercise(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    muscle_group = models.CharField(max_length=50)
    deficulty_level = models.IntegerField()

    def __str__(self):
        return self.name