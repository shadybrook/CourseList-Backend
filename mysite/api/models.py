from django.db import models

class CourseList(models.Model):
    title = models.CharField(max_length=225)
    course_code = models.CharField(max_length=20, unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"

class CourseInstance(models.Model):
    course = models.ForeignKey(CourseList, related_name='instances', on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()

    class Meta:
        unique_together = ('course', 'year', 'semester')

    def __str__(self):
        return f"{self.course.title} ({self.year} - Semester {self.semester})"