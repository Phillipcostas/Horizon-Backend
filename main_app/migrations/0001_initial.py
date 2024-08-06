# Generated by Django 4.2.14 on 2024-08-06 14:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TripPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.CharField(choices=[('Plane', 'Plane'), ('Train', 'Train'), ('Car', 'Car'), ('Boat', 'Boat')], default='Plane', max_length=255)),
                ('question_2', models.CharField(choices=[('Outdoors', 'Outdoors'), ('Relaxation', 'Relaxation'), ('Live Events', 'Live Events'), ('Work', 'Work')], default='Outdoors', max_length=255)),
                ('question_3', models.CharField(choices=[('Local', 'Local'), ('Fine Dining', 'Fine Dining'), ('Fast Food', 'Fast Food'), ('Vegetarian', 'Vegetarian')], default='Local', max_length=255)),
                ('question_4', models.CharField(choices=[('Very Often', 'Very Often'), ('Often', 'Often'), ('Once in a While', 'Once in a While'), ('Almost Never', 'Almost Never')], default='Very Often', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('interest1', models.CharField(default='')),
                ('interest2', models.CharField(default='')),
                ('interest3', models.CharField(default='')),
                ('interest4', models.CharField(default='')),
                ('profile_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profiles', to='main_app.userphoto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(default='', max_length=255)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('public', models.BooleanField(default=False)),
                ('trip_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trips', to='main_app.tripphoto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SuitcaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('packed', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('Essentials', 'Essentials'), ('Toiletries', 'Toiletries'), ('Speciality Clothes', 'Speciality Clothes'), ('Lounge Wear', 'Lounge Wear'), ('Tech', 'Tech'), ('Documents', 'Documents')], default='some-string', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('day', models.IntegerField(default=1)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='main_app.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_comment', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invited_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_invitations', to=settings.AUTH_USER_MODEL)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='main_app.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
