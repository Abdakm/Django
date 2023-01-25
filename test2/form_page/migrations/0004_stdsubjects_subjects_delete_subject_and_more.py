# Generated by Django 4.1.3 on 2022-12-24 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_page', '0003_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='StdSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_page.information')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50, verbose_name='Subject Name')),
                ('subject_number', models.CharField(max_length=30, verbose_name='Subject Number')),
            ],
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='stdsubjects',
            name='subjects',
            field=models.ManyToManyField(to='form_page.subjects'),
        ),
    ]