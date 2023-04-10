from django.shortcuts import render, get_object_or_404
from .models import Schedule


def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule/schedule_list.html',
                  {'schedules': schedules},)


def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, 'schedule/schedule_detail.html',
                  {'schedule': schedule})
