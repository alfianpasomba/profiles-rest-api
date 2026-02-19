from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("viesets-api", views.HelloViewSets, basename="viewsets")

urlpatterns = [
    path("first-api", views.HelloAPIView.as_view()),
    path("", include(router.urls))
]
