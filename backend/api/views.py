from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookModelSerializer, RegisterSerializer
from .models import Book
from rest_framework_simplejwt.tokens import RefreshToken


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    def post():
        pass


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoggoutView(APIView):
    def post(self, request):
        try:
            # Использование круглых скобок для метода .get()
            refresh_token = request.data.get("refresh")
            
            if not refresh_token:
                return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
                
            token = RefreshToken(refresh_token)
            token.blacklist() 
            
            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            # Для отладки можно временно раскомментировать строку ниже, чтобы видеть реальную ошибку в консоли:
            # print(f"Logout error: {e}")
            return Response({"error": "Invalid token or token already blacklisted."}, status=status.HTTP_400_BAD_REQUEST)