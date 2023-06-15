from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .models import *
from .forms import *
from events.models import Event

user = get_user_model()

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            
            if form.cleaned_data.get('is_athlete') == True:
                athlete = Athlete.objects.create(user=user)
                return redirect('users:profile_alert')
                        
            if form.cleaned_data.get('is_host') == True:
                host = Host.objects.create(user=user)
                return redirect('users:profile_alert')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = MyUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def profile_alert(request):
    return render(request, 'users/profile_alert.html')

@login_required
def create_athlete(request):
    form = AthleteForm()
    if request.method == 'POST':
        form = AthleteForm(request.POST, request.FILES)
        if form.is_valid():
            athlete = form.save(commit=False)
            athlete.user = request.user
            #athlete.save()
            messages.success(request, "Athlete profile created successfully!" )
            return redirect('users/ athlete_profile', pk=athlete.pk)
    return render(request, 'users/create_athlete.html', {'form': form})

@login_required
def create_host(request):
    form = HostForm()
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            host = form.save(commit=False)
            host.user = request.user
            host.save()
            messages.success(request, "Host profile created successfully!" )
            return redirect('host_profile')  
    return render(request, 'create_host.html', {'form': form})    

@login_required
def athlete_profile(request, pk):
    if request.user.is_athlete:
        #athlete = request.user.athlete
        #athlete = Athlete.objects.get(user=request.user)
        athlete = get_object_or_404(Athlete, pk=pk)
        return render(request, 'users/athlete_profile.html', {'athlete': athlete})
    else:
        return redirect('home')
    
@login_required
def host_profile(request, pk):
    if request.user.is_host:
        #host = request.user.host
        #host = Host.objects.get(user=request.user)
        host = get_object_or_404(Host, pk=pk)
        events = Event.objects.filter(host=host).order_by('-date')
        return render(request, 'users/host_profile.html', {'host': host, 'events':events})
    else:
        return redirect('home')
    
@login_required
def edit_athlete_profile(request, pk):
    if request.user.is_athlete:
        athlete = get_object_or_404(Athlete, pk=pk)
        form = AthleteForm(instance=athlete)
        if request.method == 'POST':
            form = AthleteForm(request.POST, request.FILES, instance=athlete)
            if form.is_valid():
                form.save()
                messages.success(request, "Changes saved!")
                return render(request, 'users/athlete_profile.html', {'athlete':athlete})
        return render(request, 'users/edit_athlete_profile.html', {'form': form})
    
@login_required
def edit_host_profile(request, pk):
    if request.user.is_host:
        host = get_object_or_404(Host, pk=pk)
        form = HostForm(instance=host)
        if request.method == 'POST':
            form = HostForm(request.POST, instance=host)
            if form.is_valid():
                form.save()
                messages.success(request, "Changes saved!")
                return render(request, 'users/host_profile.html', {'host':host})
        return render(request, 'users/edit_host_profile.html', {'form': form})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'users/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
    
