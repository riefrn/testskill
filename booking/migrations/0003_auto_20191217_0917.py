# Generated by Django 2.2.4 on 2019-12-17 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_bookedseat_booking_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_type',
            field=models.CharField(choices=[('', 'Select'), ('Tribun', 'Tribun')], max_length=8),
        ),
    ]
