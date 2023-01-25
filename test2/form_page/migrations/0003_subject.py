# Generated by Django 4.1.3 on 2022-12-24 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_page', '0002_alter_information_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50, verbose_name='Subject Name')),
                ('subject_number', models.CharField(max_length=20, verbose_name='Subject Number')),
            ],
        ),
    ]
