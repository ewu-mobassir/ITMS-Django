# Generated by Django 3.1.2 on 2020-12-20 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spots', '0005_auto_20201220_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='extra_per_person',
            field=models.FloatField(default=0, verbose_name='Extra cost per person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='max_no_of_people',
            field=models.IntegerField(default=10, verbose_name='maximum number of people'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='min_no_of_people',
            field=models.IntegerField(default=1, verbose_name='minimum number of people'),
        ),
        migrations.AddField(
            model_name='offer',
            name='no_of_days',
            field=models.IntegerField(default=1, verbose_name='number of days'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offered_by',
            field=models.ForeignKey(limit_choices_to={'is_agency': True}, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_people', models.IntegerField(default=1, verbose_name='number of people')),
                ('booking_time', models.DateTimeField(auto_now_add=True, verbose_name='booking time')),
                ('booked_date', models.DateTimeField(verbose_name='booked date')),
                ('total_cost', models.FloatField(verbose_name='Total Cost')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='spots.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
