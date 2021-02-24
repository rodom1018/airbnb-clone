from django.urls import path
from . import views


app_name = "login"

urlpatterns = [
    path("<int:pk", views.RoomDetail.as_view(), name="detail"),
    path("login", views.LoginView.as_view(), name="login"),
]