from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from .utils import Calendar
import calendar

from .models import *
from .utils import Calendar

# class CalendarView(generic.ListView):
#     model = Event
#     template_name = 'calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # use today's date for the calendar
#         d = get_date(self.request.GET.get('day', None))

#         # Instantiate our calendar class with today's year and date
#         cal = Calendar(d.year, d.month)

#         # Call the formatmonth method, which returns our calendar as a table
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)

#         d = get_date(self.request.GET.get('month', None))
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)

#         return context

def fucking_calendar(request, date = None):
    context = {}
    print("date on line 38", date)
    d = get_date(request.GET.get('day', None))
    m = request.GET.get('month', None)

    if date != "favicon.ico" and None:
        print(date)
        date = date.split("-")
        print("date on 45", date)
        date = f"{date[0]}-{date[1]}"
        d = get_date(date)
        print("in the if statement",d.year, d.month)
        m = date
    # use today's date for the calendar

    # Instantiate our calendar class with today's year and date
    cal = Calendar(d.year, d.month)

    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_cal)

    # d = get_date(m)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)
    return render(request, "calendar.html", context)

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        # print(date(year, month, day=1))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    year = d.year
    month = d.month
    days_in_month = calendar.monthrange(year, month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = str(next_month.year) + '-' + str(next_month.month)
    return month