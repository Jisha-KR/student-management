from django.urls import path
#from . import views
from . views import *

'''
urlpatterns = [
    path('student_list_create/',views.student_list_create,name='student_list_create'),
    path('course_list_create/',views.course_list_create,name='course_list_create'),
]
'''

urlpatterns =[
    path('student_list_create/',StudentListCreate.as_view(),name='student_list_create'),
    path("student_detail_view/<int:pk>/",StudentDetailView.as_view(),name="student_detail_view"),
    path('course_list_create/',CourseListCreate.as_view(),name='course_list_create'),
    path('course_list_view/<int:pk>/',CourseListView.as_view(),name='course_list_view'),
]