from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)
