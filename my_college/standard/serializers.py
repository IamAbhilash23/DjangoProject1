from rest_framework import serializers
from standard.models import Section,Student


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    section_id=serializers.ReadOnlyField()
    class Meta:
        model=Section
        fields="__all__"
class StudentSerializer(serializers.HyperlinkedModelSerializer):

    id=serializers.ReadOnlyField()
    class Meta:
        model=Student
        fields="__all__"
