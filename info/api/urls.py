from django.urls import path

from .views import (CaseStudyRetrieveAPIView, CaseStudyListAPIView, CaseStudySectionListAPIView,
                    DribbleWorkSectionListAPIView)


app_name = 'info'

urlpatterns = [
    path('case-study/<int:pk>/', CaseStudyRetrieveAPIView.as_view(), name='case-study'),
    path('case-studies/', CaseStudyListAPIView.as_view(), name='case-studies'),
    path('case-study-sections/', CaseStudySectionListAPIView.as_view(), name='case-study-sections'),
    path('dribble-works/', DribbleWorkSectionListAPIView.as_view(), name='dribble-works'),
]
