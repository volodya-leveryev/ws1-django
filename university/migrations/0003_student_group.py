# Generated by Django 5.0.2 on 2024-02-08 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_group_options_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.group', verbose_name='группа'),
        ),
    ]
