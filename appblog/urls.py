from django.urls import path

from .views import post_list

app_name = "appblog"

urlpatterns = [
    path('', post_list)
]