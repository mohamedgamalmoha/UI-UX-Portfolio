from rest_framework.generics import ListAPIView

from info.models import CaseStudy, CaseStudySection, DribbleWork
from .filters import CaseStudySectionFilter
from .serializers import CaseStudySerializer, CaseStudySectionSerializer, DribbleWorkSerializer


class CaseStudyAPIView(ListAPIView):
    queryset = CaseStudy.objects.active()
    serializer_class = CaseStudySerializer


class CaseStudySectionAPIView(ListAPIView):
    queryset = CaseStudySection.objects.active()
    serializer_class = CaseStudySectionSerializer
    filterset_class = CaseStudySectionFilter


class DribbleWorkSectionAPIView(ListAPIView):
    queryset = DribbleWork.objects.active()
    serializer_class = DribbleWorkSerializer
