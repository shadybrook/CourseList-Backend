from rest_framework import generics, status
from rest_framework.response import Response
from .models import CourseList
from .serializers import CourseListSerializer
from .serializers import CourseInstanceSerializer
from .models import CourseInstance

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = CourseList.objects.all()
    serializer_class = CourseListSerializer

    def delete(self, request, *args, **kwargs):
        CourseList.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseList.objects.all()
    serializer_class = CourseListSerializer
    lookup_field = "pk"

class CourseInstanceCreateView(generics.CreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['course'] = int(data['course_id'])  # Assuming course_id is provided in the request data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CourseInstanceListView(generics.ListAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)

class CourseInstanceRetrieveView(generics.RetrieveAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        course_id = self.kwargs['course_id']
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.get(course_id=course_id, year=year, semester=semester)

class CourseInstanceDeleteView(generics.DestroyAPIView):
    def get_object(self):
        course_id = self.kwargs['course_id']
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.get(course_id=course_id, year=year, semester=semester)