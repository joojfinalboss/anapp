from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Create your views here.
class RegisterView(views.APIView):
    def post(self, request):
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            return Response({"status": "success"})
        else:
            return Response({"status": "error", "errors": form.errors})

class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"status": "success", "token": token.key})
        else:
            return Response({"status": "error", "message": "Invalid username or password"})

class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response("Logged out successfully")

class ProtectedView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("You are seeing this because you are logged in")