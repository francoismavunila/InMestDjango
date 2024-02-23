from django.shortcuts import render
from django.http  import HttpResponse, JsonResponse
from django.core import serializers

from users.serializers import *
from  .models import *

# Create your views here.
def  index(request):
    return HttpResponse("Hie I am the user")
def user_profile(request):
    return JsonResponse({
        "name": "John Doe",
        "email":"example@gmail.com",
        "phone_number": "0986767682628767"
    })

def get_cohort(request):
    cohort = Cohort.objects.get(id=3)
    serialized_cohort = CohortSerializer(cohort)
    print(serialized_cohort)
    return  JsonResponse(serialized_cohort.data, safe=False)
    

def get_user(request):
    user = IMUser.objects.get(id=10)
    print(user)
    serializer_user = UserSerializer(user, many=False)
    print(serializer_user.data)
    return JsonResponse(
     serializer_user.data
    )

def get_cohort_member(request):
    CohorMembers = CohorMember.objects.filter(id = 2)
    print(CohorMembers)
    serialized_members = CohortMemberSerializer(CohorMembers, many = True)
    print(serialized_members.data)
    return JsonResponse({'cohor members': serialized_members.data})
