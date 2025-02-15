from django.http import HttpResponse
from django.http import JsonResponse
from .business.auth import AuthBusiness


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AuthenticateView(APIView):
    def post(self, request):
        try:
            auth_business = AuthBusiness()
            auth_response = auth_business.authenticate(request)
            return Response({"message": "Authentication successful", "data": auth_response}, status=status.HTTP_200_OK)
            #print("OOOK")
            #
            #return Response({"message": "Authentication successful", "data": auth_response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
