from math import ceil
from django.shortcuts import render
from djnago.core.paginator import Paginator
from . import models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    return render(request, "rooms/home.html", {})
