from django.db import models

class Activity(models.Model):
    """A days all activitys"""
    date = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ('date',)
        verbose_name = 'activity'
        verbose_name_plural  = 'activities'

    def __str__(self):
        return self.date




class ActivityType(models.Model):
    """Type of the activity, e.g. ride, hike"""

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name




class Ride(models.Model):
    type = models.ForeignKey(ActivityType, related_name='rides', on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()
    elev_gain = models.IntegerField()
    avg_speed = models.DecimalField(max_digits=6, decimal_places=2)
    cal_burned = models.IntegerField()

    created = models.TimeField(auto_now_add=True)
