
from rest_framework.decorators import api_view as shop_api
from rest_framework.response import Response
from .serializers import RegisterSerializer, ConfirmSerializer, LoginSerializer
from .models import Confirm
from rest_framework.views import APIView

class RegisterAPIView(APIView):
    def post (self, request):
     serializer = RegisterSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     result = serializer.save()
     return Response({
        "message": "User created",
        "code": result["code"]
    })
class ConfirmAPIView(APIView):
    def post(self, request):
     serializer = ConfirmSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     user = serializer.validated_data
     user.is_active = True
     user.save()
     Confirm.objects.get(user=user).delete()
     return Response({"message": "User confirmed"})
 
class LoginAPIView(APIView):
    def post(self, request):
     serializer = LoginSerializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     return Response({"message": "Login success"})
