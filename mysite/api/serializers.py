from rest_framework import serializers
from .models import CourseList 
from .models import CourseInstance



class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseList
        fields = '__all__'


class CourseInstanceSerializer(serializers.ModelSerializer):
    course = CourseListSerializer

    class Meta:
        model=CourseInstance
        fields = '__all__'