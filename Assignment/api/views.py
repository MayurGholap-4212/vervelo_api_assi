from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from.permissions import *
# Create your views here.

class QuestionViewset(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializers
    permission_classes=[IsStaffOrSuperAdmin]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by=self.request.user)
        
    def perform_update(self, serializer):
        return serializer.save(updated_by=self.request.user)
    
    
class AssessmentViewset(viewsets.ModelViewSet):
    queryset=Assessment.objects.all()
    serializer_class=AssessmentSerializers
    permission_classes=[IsStaffOrSuperAdmin]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by=self.request.user)
        
    def perform_update(self, serializer):
        return serializer.save(updated_by=self.request.user)
    
    
class AssignAssessmentViewset(viewsets.ModelViewSet):
    queryset=AssignAssessment.objects.all()
    serializer_class=AssignAssessmentSerializers
    # permission_classes=[IsAssignedOrReadOnly]
        
    def get_queryset(self):
        user = self.request.user
        if getattr(user, 'is_staff', False) or getattr(user, 'is_super_admin', False):
            return AssignAssessment.objects.all()
        return AssignAssessment.objects.filter(user=user)
