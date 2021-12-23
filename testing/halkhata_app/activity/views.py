from django.db.models.fields import DateField
from django.shortcuts import render, redirect
from .models import Ride, Run, Walk, Activity
from .forms import AddRideForm
from django.shortcuts import get_object_or_404, HttpResponse
import datetime

def activity_list(request):
    dates = Activity.objects.all()
    
    activities = []

    for date in dates:
        for walk in date.walks.all():
            activities.append(walk)
        for run in date.runs.all():
            activities.append(run)
        for ride in date.rides.all():
            activities.append(ride)
    print(activities)

    return render(request, 'activity/activity_list.html',{'activities':activities})



def activity_details(request, type, id):

    if type == 'ride':

        activity = get_object_or_404(Ride, pk = id)

    elif type == 'walk':
    
        activity = get_object_or_404(Walk, pk = id)

    elif type == 'run':
    
        activity = get_object_or_404(Run, pk = id)


    return render(request, 'activity/activity_detail_ride.html', {'activity':activity})


def add_activity (request, type = None):
    #If it's a new day then create a new Activity object
    if not Activity.objects.all():
        latest_activity = Activity()
        latest_activity.save()
        

    elif Activity.objects.all():
        latest_activity = Activity.objects.all()[0]
     
        if latest_activity.date != datetime.datetime.now().date():
            latest_activity = Activity()
            latest_activity.save()

    #add the new activity according to its type.
    time_now = datetime.datetime.now().time()
    today = datetime.datetime.now().date()

    if type=='ride':
        if request.method != 'POST':
            form = AddRideForm()
        else:
            form = AddRideForm(data=request.POST)
            print('here')
            if form.is_valid():
                print("valid\n")
                new_ride = form.save(commit=False)
                new_ride.date = latest_activity
                new_ride.save()
                return redirect(new_ride)
            
        return render(request, 'activity/add_ride.html', {'form':form, 'date':today, 'time':time_now})


    return render(request, 'activity/add_activity.html')