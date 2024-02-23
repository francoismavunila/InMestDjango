from rest_framework import serializers

from users.models import IMUser

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    # def create(self, validated_data):
    #     return IMUser.objects.create(**validated_data)

class CohortSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    is_active = serializers.BooleanField(default = False)
    author = UserSerializer(many=False)

class CohortMemberSerializer(serializers.Serializer):
    cohort = CohortSerializer(many=False)
    member = UserSerializer(many = False)
    author = UserSerializer(many = False)