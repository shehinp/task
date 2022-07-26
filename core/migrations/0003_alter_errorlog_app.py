# Generated by Django 4.0.1 on 2022-01-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_errorlog_detail_alter_settings_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlog',
            name='app',
            field=models.SlugField(blank=True, choices=[('na', 'N/a'), ('core', 'Core'), ('core', 'Core'), ('lead', 'Lead'), ('user', 'User')], default='na', max_length=20, null=True, verbose_name='app'),
        ),
    ]