from django.urls import path
from . import views

urlpatterns = [
    # path("calendar", views.CalendarView.as_view(), name='calendar'), # here
    path("", views.fucking_calendar, name = 'calendar'),
    path("<str:date>", views.fucking_calendar, name = 'calendar'),
]