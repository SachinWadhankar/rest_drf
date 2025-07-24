from django.contrib import admin
from django.urls import path, include
from drf_app.views import TwoWheelarViewSet
from rest_framework.routers import SimpleRouter

tw_router = SimpleRouter()
tw_router.register(r'Bikes', TwoWheelarViewSet)



urlpatterns = [
    path('',include(tw_router.urls) ),
]