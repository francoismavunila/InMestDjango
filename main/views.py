from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import ClassSchedule
from main.serializers import ClassScheduleSerializer




# Create your views here.
def say_hello(request):
    return HttpResponse("<h1>Hie my friends on youtube</h1>")

def filter_queries(request, id):
    user = [user for user in users if int(user['id']) == int(id)]
    if user:
        return JsonResponse(user[0])
    else:
        return HttpResponse("user not found")
    
class QueryView(View):
    users = [
        {"name": "Alice", "age":  30, "city": "New York", "id":  1},
        {"name": "Bob", "age":  25, "city": "Los Angeles", "id":  2},
        {"name": "Charlie", "age":  28, "city": "Chicago", "id":  3},
        {"name": "Diana", "age":  35, "city": "San Francisco", "id":  4}
    ]
    def get(self, request):
        return JsonResponse({"users": self.users})
    def post(self, request):
        return JsonResponse({"status":"done"})

@api_view(["GET"])
def fetch_class_schedule(request):
    query_set = ClassSchedule.objects.all()
    serializer = ClassScheduleSerializer(query_set, many=True)
    return Response({"data": serializer.data}, status.HTTP_200_OK)

@api_view(["POST"])
def create_class_schedule(request):
    