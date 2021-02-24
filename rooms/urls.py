from django.urls import path
from rooms import views as rooms_views

app_name = "rooms"

urlpatterns = [
    path("", rooms_views.HomeView.as_view(), name="basic"),
    path("<int:pk>", rooms_views.HomeView.as_view(), name="detail"),
    path("search/", rooms_views.search, name="search"),
]
