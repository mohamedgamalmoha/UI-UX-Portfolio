from django.urls import path

from .views import CaseStudyAPIView, CaseStudySectionAPIView, DribbleWorkSectionAPIView


app_name = 'info'

urlpatterns = [
    path('case-studies/', CaseStudyAPIView.as_view(), name='case-study'),
    path('case-study-sections/', CaseStudySectionAPIView.as_view(), name='case-study-section'),
    path('dribble-works/', DribbleWorkSectionAPIView.as_view(), name='dribble-work'),
]
