# Generated by Django 4.0.5 on 2022-06-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salepost',
            name='imag3',
            field=models.ImageField(blank=True, default='pictures/picture.png', null=True, upload_to='views'),
        ),
        migrations.AlterField(
            model_name='salepost',
            name='image1',
            field=models.ImageField(blank=True, default='pictures/picture.png', null=True, upload_to='views'),
        ),
        migrations.AlterField(
            model_name='salepost',
            name='image2',
            field=models.ImageField(blank=True, default='pictures/picture.png', null=True, upload_to='views'),
        ),
    ]
