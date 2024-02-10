from django.shortcuts import render
from django.http  import HttpResponse, JsonResponse

# Create your views here.
def  index(request):
    return HttpResponse("Hie I am the user")
def user_profile(request):
    return JsonResponse({
        "name": "John Doe",
        "email":"example@gmail.com",
        "phone_number": "0986767682628767"
    })
