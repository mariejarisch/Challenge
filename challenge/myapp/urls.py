from django.urls import path
from .views import input_view

urlpatterns = [
    # route to input_view where user inpput can happen
    path("", input_view, name="input"),
]
