from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .forms import EditprofileForm, LoginForm, SignupForm, RegistrationForm, EventForm
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return HttpResponse("Hello")


@login_required
def dashboard(request):
    user = request.user
    events = Event.objects.all()
    my_events = Event.objects.filter(created_by=user)
    return render(request, 'event/dashboard.html', {'user':user, 'events':events, 'my_events':my_events})


def auth_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
        
    else:
        form = LoginForm()
    return render(request, 'event/login.html', {'form':form})

def auth_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        
    else:
        form = SignupForm()
    return render(request, 'event/signup.html', {'form':form})
        


def auth_logout(request):
    logout(request)
    return redirect('login')


    

def allevents(request):
    events = Event.objects.all()
    return render(request, "event/events.html", {'events':events})


def event_detail(request, pk):
    detail = get_object_or_404(Event, pk=pk)
    events = Event.objects.all()
    return render(request, 'event/event_detail.html', {'detail':detail, 'events':events})

@login_required
def event_creation(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events')
        
    else:
        form = EventForm()
    return render(request, 'event/event_creation.html', {'form':form})






def registration(request, pk):
    if request.method == "POST":
        event = Event.objects.get(pk=pk)

        if Registration.objects.filter(user_id=request.user, event_id=event).exists():
            messages.info(request, "You have already registered for this event.")
        else:
            Registration.objects.create(
                user_id=request.user,
                event_id=event
            )
            messages.success(request, "You have successfully registered for this event!")

        return redirect("my_registrations")
    


def registrationlist(request):
    register = Registration.objects.filter(user_id=request.user)

    return render(request, 'event/my_registrations.html', {'register':register})





def deleteevent(request, pk):
    event = get_object_or_404(Registration, pk=pk, user_id=request.user)
    event.delete()
    messages.success(request, "Registration deleted successfully.")
    return redirect("my_registrations")





def editprofile(request):
    if request.method == 'POST':
        form = EditprofileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = EditprofileForm(instance=request.user) 

    return render(request, 'event/editprofile.html', {'form': form})