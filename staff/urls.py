from django.urls import path
from . import views
urlpatterns = [
    path('staff/', views.staff_view , name='staff_view'),
    # path('staffselected/', views.staff_accept_view , name='staff_accept_view'),
    path('staff/acceptedstudents/', views.accept_view, name='accept_view'),
    #path('staff/rejectedstudents/', views.reject_view, name='reject_view'),



    ]