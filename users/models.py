from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# profile - [phone,mobile,dob, ]
# address   [st,pin]


class Profile(models.Model):

    USER_TYPES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    GENDER_TYPES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='userprofile', null=True)
    Gender = models.SlugField(default='male', choices=GENDER_TYPES, max_length=20)
    DOB = models.DateField(null=True, blank=True)
    Address = models.TextField(max_length=256, null=True, blank=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Usertype = models.SlugField(default='user', choices=USER_TYPES, max_length=20)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + self.Usertype

class Teacher(models.Model):

    student = models.ForeignKey('auth.user', verbose_name=_("Student"), on_delete = models.CASCADE, related_name='my_student',  null=True, blank=True)
    teacher = models.ForeignKey('auth.user', verbose_name=_("Teacher"), on_delete = models.CASCADE, related_name='my_teacher',  null=True, blank=True) 
    isactive= models.BooleanField(default=True)
    addedAt = models.DateTimeField(verbose_name=_("Added at"),auto_now_add=True, null=True)    
    updatedAt = models.DateTimeField(verbose_name=_("Updated at"),auto_now=True, null=True)