# Generated by Django 4.0.1 on 2022-06-12 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_remove_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_student', to=settings.AUTH_USER_MODEL, verbose_name='Student'),
        ),
    ]
