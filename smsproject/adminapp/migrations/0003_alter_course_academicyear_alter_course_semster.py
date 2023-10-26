# Generated by Django 4.2.4 on 2023-09-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_course_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='academicyear',
            field=models.CharField(choices=[('2023-24', '2023-24'), ('2024-25', '2024-25'), ('2025-26', '2025-26')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='semster',
            field=models.CharField(choices=[('odd', 'odd'), ('even', 'even')], max_length=10),
        ),
    ]
