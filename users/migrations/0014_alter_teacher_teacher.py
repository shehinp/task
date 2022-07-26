# Generated by Django 4.0.1 on 2022-06-12 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0013_teacher_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_student', to=settings.AUTH_USER_MODEL, verbose_name='Teacher'),
        ),
    ]
