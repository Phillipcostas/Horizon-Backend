from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Trip, Itinerary


def about(request):
    return render(request, "base.html")


def about(request):
    return render(request, "map.html")


def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trip.html', { 'trips': trips })

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userProfile = UserProfile.objects.create(user=user, name=user.username)
            userProfile.save()
            return redirect("home")
        else:
            error_message = "Invalid sign up - try again"
    else:
        form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)

@login_required
def calendar_view(request):
    events = Event.objects.filter(user=request.user)
    form = EventForm()
    return render(request, 'calendar.html', {'events': events, 'form': form})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'calendar.html', {'form': form})

class Home(LoginView):
    template_name = "home.html"


class Login(LoginView):
    template_name = 'login.html'


class Map(LoginView):
    template_name = "map.html"


class Trip(LoginView):
    template_name = "trip.html"


class AddTrip(LoginView):
    template_name = "addTrip.html"

