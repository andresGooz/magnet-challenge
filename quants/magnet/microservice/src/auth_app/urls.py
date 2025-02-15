from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("", views.index, name="index"),
]