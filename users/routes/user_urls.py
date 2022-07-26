
from django.urls import re_path

from ..views.student_views import viewteacher
from ..views.teacher_views import viewstudent

urlpatterns = [
    re_path(r'teacherviewstudent', viewstudent, name='teacherviewstudent'),
    re_path(r'studentviewteacher', viewteacher, name='studentviewteacher'),
    
]