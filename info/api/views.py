from rest_framework.generics import RetrieveAPIView, ListAPIView

from info.models import CaseStudy, CaseStudySection, DribbleWork
from .filters import CaseStudySectionFilter
from .serializers import CaseStudySerializer, CaseStudySectionSerializer, DribbleWorkSerializer


class CaseStudyRetrieveAPIView(RetrieveAPIView):
    queryset = CaseStudy.objects.active()
    serializer_class = CaseStudySerializer


class CaseStudyListAPIView(ListAPIView):
    queryset = CaseStudy.objects.active()
    serializer_class = CaseStudySerializer


class CaseStudySectionListAPIView(ListAPIView):
    queryset = CaseStudySection.objects.active()
    serializer_class = CaseStudySectionSerializer
    filterset_class = CaseStudySectionFilter


class DribbleWorkSectionListAPIView(ListAPIView):
    queryset = DribbleWork.objects.active()
    serializer_class = DribbleWorkSerializer
