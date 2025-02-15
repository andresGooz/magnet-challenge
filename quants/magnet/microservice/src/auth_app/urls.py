from django.urls import path
#from django.urls import include
from .views import AuthenticateView


urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    path('', AuthenticateView.as_view(), name='authenticate'),
]