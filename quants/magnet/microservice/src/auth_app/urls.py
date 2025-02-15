from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('api-auth/', include('rest_framework.urls'))
]