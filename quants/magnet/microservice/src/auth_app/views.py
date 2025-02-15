from django.http import HttpResponse
from django.http import JsonResponse
from .business.auth import AuthBusiness


def index(request):
    return HttpResponse("Hello, world AUTH. You're at the polls index. :)")

def authenticate_view(request):
    try:
        auth_business = AuthBusiness()
        auth_response = auth_business.authenticate(request)
        return JsonResponse({"message": "Authentication successful", "data": auth_response}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)