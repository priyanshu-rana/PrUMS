# Generated by Django 5.0.3 on 2024-03-10 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('head_of_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_headed', to='ums.teacher')),
            ],
        ),
    ]
