import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Event, Registration
from users.models import *
from .forms import EventForm, EventRegistrationForm
import pandas as pd, io
from django.http import HttpResponse

user = get_user_model()

def event_list(request):
    events = Event.objects.all().order_by('-published_date')
    return render(request, 'event/post_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    print(event.host)
    print(request.user)
    context = {
        'now': datetime.datetime.now(),
        'event': event
    }
    
    return render(request, 'event/post_details.html', context)

@login_required
def event_create(request):
    if not request.user.is_host:
        messages.warning(request, "You don't have permission to create events.")
        return redirect('post_list')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user.host
            event.save()
            messages.success(request, 'Event created successfully.')
            return render(request, 'event/post_details.html', {'event': event})
    else:
        form = EventForm()
    return render(request, 'event/event_create.html', {'form': form})

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user.host != event.host:
        messages.warning(request, "You don't have permission to update this event.")
        return redirect('event_detail', pk=event.pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.success(request, 'Event updated successfully.')
            return render(request, 'event/post_details.html', {'event': event})
    else:
        form = EventForm(instance=event)
    return render(request, 'event/event_update.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    messages.success(request, 'Event deleted successfully.')
    return render(request, 'event/post_list.html', {'event': event})

def event_registration(request, pk):
    athlete = Athlete.objects.get(user=request.user)
    event = Event.objects.get(pk=pk)
    today = datetime.date.today()

    if Registration.objects.filter(event=event, athlete=athlete).exists():
        return HttpResponse("You have already registered for this event.")

    if today > event.last_reg_date:
        return redirect('events:reg_closed')
    else:
        if request.method == 'POST':
            form = EventRegistrationForm(request.POST)
            if form.is_valid():
                registration = event.registration_set.create(
                    athlete=athlete,
                    name=form.cleaned_data['name'],
                    contact_number=form.cleaned_data['contact_number'],
                    age=form.cleaned_data['age'],
                    gender=form.cleaned_data['gender'],
                    height=form.cleaned_data['height'],
                    weight=form.cleaned_data['weight'],
                    weight_category=form.cleaned_data['weight_category'],
                    fighting_style=form.cleaned_data['fighting_style'],
                    club_name=form.cleaned_data['club_name']
                )
                return redirect('events:registration_success', registration_id=registration.id, pk=athlete.pk)
        else:
            form = EventRegistrationForm(initial={
                'event': event,
                'name': athlete.name,
                'contact_number': athlete.contact_number,
                'age': athlete.age,
                'gender': athlete.gender,
                'height': athlete.height,
                'weight': athlete.weight,
                'weight_category': athlete.weight_category,
                'fighting_style': athlete.fighting_style,
                'club_name': athlete.club_name,
            })
        return render(request, 'event/event_registration.html', {'form': form})

def reg_closed(request):
    return render(request, 'event/reg_closed.html')

def registration_success(request, registration_id, pk):
    registration = Registration.objects.get(id=registration_id)
    athlete = registration.athlete
    event = registration.event

    context = {
        'event': event,
        'registration': registration,
        'athlete': registration.athlete
    }
    return render(request, 'event/registration_success.html', context)

@login_required
def view_registrations(request, pk):
    event = Event.objects.get(pk=pk)
    registrations = Registration.objects.filter(event=event).order_by('age', 'weight')
    context = {
        'event': event,
        'registrations': registrations
    }
    return render(request, 'event/view_registrations.html', context)

@login_required
def download_registrations(request, event_id):
    registrations = Registration.objects.filter(event_id=event_id)
    data = {
        'Name': [r.name for r in registrations],   
        'Age': [r.age for r in registrations],
        'Gender': [r.gender for r in registrations],
        'Height': [r.height for r in registrations],
        'Weight': [r.weight for r in registrations],
        'Weight Category': [r.weight_category for r in registrations],
        'Contact Number': [r.contact_number for r in registrations],
        'Fighting Style': [r.fighting_style for r in registrations],
        'Club Name': [r.club_name for r in registrations],
    }
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="registrations.xlsx"'
    with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    return response
