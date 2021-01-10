from django.urls import include, path
from . import views


urlpatterns = [
    # django-allauth
    path("", include("allauth.urls")),
    path("profile/", views.profile),
]