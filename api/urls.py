from django.urls import path,include
from.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('question',QuestionViewset)
router.register('assessment',AssessmentViewset)
router.register('assignments',AssignAssessmentViewset)
router.register('userregister',UserRegisterViewset)

urlpatterns = [
    path('',include(router.urls)),
]
