# Generated by Django 4.1.3 on 2023-01-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]