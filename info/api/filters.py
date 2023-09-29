from django_filters import rest_framework as filters

from info.models import CaseStudySection


class CaseStudySectionFilter(filters.FilterSet):

    class Meta:
        model = CaseStudySection
        fields = ('case_study', 'is_active')
