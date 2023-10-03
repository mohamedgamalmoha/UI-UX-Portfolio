from django.urls import path

from .views import CaseStudyListAPIView, CaseStudySectionListAPIView, DribbleWorkSectionListAPIView


app_name = 'info'

urlpatterns = [
    path('case-studies/', CaseStudyListAPIView.as_view(), name='case-study'),
    path('case-study-sections/', CaseStudySectionListAPIView.as_view(), name='case-study-section'),
    path('dribble-works/', DribbleWorkSectionListAPIView.as_view(), name='dribble-work'),
]
