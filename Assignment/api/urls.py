from django.urls import path,include
from.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('question',QuestionViewset)
router.register('Assessment',AssessmentViewset)
router.register('Assignments',AssignAssessmentViewset)
router.register('UserRegister',UserRegisterViewset)

urlpatterns = [
    path('',include(router.urls)),
]
