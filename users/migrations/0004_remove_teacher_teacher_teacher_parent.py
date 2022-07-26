# Generated by Django 4.0.1 on 2022-06-12 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_profile_usertype_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_teacher', to=settings.AUTH_USER_MODEL, verbose_name='Parent'),
        ),
    ]