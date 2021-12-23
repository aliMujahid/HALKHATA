from django.urls import path
from . import views


app_name = 'activity'

urlpatterns = [
    path('list/', views.activity_list, name='activity_list'),
    path('detail/<str:type>/<int:id>/', views.activity_details, name='activity_details'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('add_activity/<str:type>/', views.add_activity, name='add_activity_by_type'),

]
