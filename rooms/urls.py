from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.HomeView.as_view(), name="detail"),
    path("search/", views.search, name="search"),
]
