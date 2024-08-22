from django.urls import path
from . import views

urlpatterns = [
    path("CourseList/", views.CourseListCreateView.as_view(), name="CourseList-view-create"),
    
    path ("CourseList/<int:pk>/",
         views.CourseListRetrieveUpdateDestroyView.as_view(),
         name='update'),

    path('instances/', views.CourseInstanceCreateView.as_view(), name='course-instance-create'),
    path('instances/<int:year>/<int:semester>/', views.CourseInstanceListView.as_view(), name='course-instance-list'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', views.CourseInstanceRetrieveView.as_view(), name='course-instance-retrieve'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/delete/', views.CourseInstanceDeleteView.as_view(), name='course-instance-delete')
]

