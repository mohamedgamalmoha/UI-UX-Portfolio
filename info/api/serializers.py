from rest_framework import serializers

from info.models import CaseStudy, CaseStudySection, DribbleWork


class CaseStudySectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseStudySection
        exclude = ()


class CaseStudySerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseStudy
        exclude = ()


class DribbleWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DribbleWork
        exclude = ()
