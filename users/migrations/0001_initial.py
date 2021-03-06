# Generated by Django 4.0.1 on 2022-01-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.SlugField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Address', models.TextField(blank=True, max_length=256, null=True)),
                ('Phone', models.CharField(blank=True, max_length=15, null=True)),
                ('Usertype', models.SlugField(choices=[('user', 'User'), ('lead', 'Lead'), ('admin', 'Admin')], default='user', max_length=20)),
            ],
        ),
    ]
