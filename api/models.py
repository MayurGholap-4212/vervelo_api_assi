from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_super_admin=models.BooleanField(default=False)
    

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
    ('single_select', 'Single Select'),
    ('multi_select', 'Multi Select'),
    ('short_text', 'Short Text'),
    ('long_text', 'Long Text'),
    ]
    title=models.CharField(max_length=255)
    description=models.TextField()
    question_type=models.CharField(max_length=20,choices=QUESTION_TYPE_CHOICES)
    choices=models.JSONField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='created_questions')
    updated_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='updated_questions')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
        
class Assessment(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    questions=models.ManyToManyField(Question)
    is_active=models.BooleanField(default=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='created_assingments')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='updated_assignments')
    updated_at=models.DateTimeField(auto_now_add=True)

class AssignAssessment(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='assigned_assessments')
    assessment=models.ForeignKey(Assessment,on_delete=models.CASCADE)
    assigned_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='assigned_by')
    attempted_questions=models.IntegerField(default=0)
    correct_question=models.IntegerField(default=0)
    incorrect_questions=models.IntegerField(default=0)