# Generated by Django 4.0.3 on 2022-06-11 08:12

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=24)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stafflogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('rpassword', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(max_length=40)),
                ('lastname', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Salepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], default='Draft', max_length=50)),
                ('property_type', models.TextField(max_length=10)),
                ('area_type', models.TextField(max_length=10)),
                ('floor', models.TextField(max_length=10)),
                ('total_floor', models.TextField(max_length=10)),
                ('property_age', models.TextField(max_length=10)),
                ('property_status', models.TextField(max_length=10)),
                ('land_mark', models.TextField(max_length=10)),
                ('location', models.TextField(max_length=10)),
                ('selling_price', models.TextField(max_length=10)),
                ('date', models.DateField(blank=True, max_length=5, null=True)),
                ('furnishing', models.TextField(max_length=10)),
                ('description', models.TextField(max_length=20)),
                ('image', models.FileField(upload_to='views')),
                ('video', models.FileField(upload_to='')),
                ('areasqt', models.TextField(max_length=4)),
                ('multiple', models.TextField(max_length=4)),
                ('Buy', models.CharField(max_length=10)),
                ('lift', models.CharField(blank=True, max_length=10, null=True)),
                ('gym', models.CharField(blank=True, max_length=10, null=True)),
                ('swimmingpool', models.CharField(blank=True, max_length=10, null=True)),
                ('petsallowed', models.CharField(blank=True, max_length=10, null=True)),
                ('wifiinternet', models.CharField(blank=True, max_length=10, null=True)),
                ('childrenPlayground', models.CharField(blank=True, max_length=10, null=True)),
                ('twowheeler', models.CharField(blank=True, max_length=10, null=True)),
                ('fourwheeler', models.CharField(blank=True, max_length=10, null=True)),
                ('towfourwheeler', models.CharField(blank=True, max_length=10, null=True)),
                ('gateaccess', models.CharField(blank=True, max_length=10, null=True)),
                ('balcony', models.CharField(blank=True, max_length=10, null=True)),
                ('image1', models.FileField(blank=True, null=True, upload_to='views')),
                ('image2', models.FileField(blank=True, null=True, upload_to='views')),
                ('new_slug', autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='property_type', unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rentpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], default='Draft', max_length=50)),
                ('property_type', models.TextField(max_length=1)),
                ('area_type', models.TextField(max_length=1)),
                ('floor', models.TextField(max_length=1)),
                ('totalfloor', models.TextField(max_length=1)),
                ('propertyage', models.TextField(max_length=1)),
                ('propertystatus', models.TextField(max_length=1)),
                ('landmark', models.TextField(max_length=1)),
                ('location', models.TextField(max_length=1)),
                ('askingrent', models.TextField(max_length=1)),
                ('askingdeposite', models.TextField(max_length=1)),
                ('date', models.DateField(max_length=5)),
                ('furnishing', models.TextField(max_length=1)),
                ('description', models.TextField(max_length=1)),
                ('image', models.FileField(upload_to='media')),
                ('video', models.FileField(upload_to='media')),
                ('areasqt', models.TextField(max_length=1)),
                ('multiple', models.TextField(max_length=1)),
                ('rent', models.CharField(max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
