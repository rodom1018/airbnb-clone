from django.views.generic import ListView, DetailView
from django.shortcuts import render
from rooms import models

# Create your views here.


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


"""
class RoomDetail(DetailView):
    RoomDetail Definition

    model = models.Room
    context_object_name = "rooms"
    """


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
