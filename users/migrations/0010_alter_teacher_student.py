# Generated by Django 4.0.1 on 2022-06-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_teacher_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='student',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]