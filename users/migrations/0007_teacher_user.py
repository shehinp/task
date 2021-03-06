# Generated by Django 4.0.1 on 2022-06-12 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_alter_profile_usertype_alter_teacher_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enroll_student', to=settings.AUTH_USER_MODEL, verbose_name='teacher'),
        ),
    ]
