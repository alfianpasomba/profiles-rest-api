from django.urls import path
from profiles_api import views

urlpatterns = [
    path("first-api", views.HelloAPIView.as_view())
]
