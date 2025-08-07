from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'first_name', 'last_name', 'email', 'is_staff', 'is_super_admin']
    
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