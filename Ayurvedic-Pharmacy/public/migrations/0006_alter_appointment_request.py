# Generated by Django 4.2.3 on 2023-07-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_appointment_accepted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='request',
            field=models.TextField(blank=True, null=True),
        ),
    ]
