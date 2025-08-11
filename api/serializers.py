from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'first_name', 'last_name','username','password', 'email']
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data.pop('password', None)
        if password:
            user.set_password(password)  
        user.is_staff = False
        user.is_super_admin = False
        user.save()
        return user
    
class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'
    
class AssessmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Assessment
        fields='__all__'
    
class AssignAssessmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=AssignAssessment
        fields='__all__'