
from django.urls import re_path
from ..views.core_views import  addstudent, addteacher, assignteacher, dashboard, register, viewstudent, xlogin, xlogout

urlpatterns = [
    re_path(r'register', register, name="register"),
    re_path(r'login/', xlogin, name="login"),
    re_path(r'dashboard', dashboard, name='dashboard'),
    re_path(r'logout', xlogout, name="logout"),

    re_path(r'addstudent', addstudent, name="addstudent"),
    re_path(r'addteacher', addteacher, name="addteacher"),
    re_path(r'viewstudent', viewstudent, name='viewstudent'),
    re_path(r'assignteacher', assignteacher, name='assignteacher'),
]