from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RegisterViewSet


# urlpatterns = [
#
#     path("register/", UserViewSet.as_view()),
#
# ]