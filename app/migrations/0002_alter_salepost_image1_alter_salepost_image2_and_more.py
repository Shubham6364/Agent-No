# Generated by Django 4.0.5 on 2022-07-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salepost',
            name='image1',
            field=models.ImageField(blank=True, default='media/views/default.jpg', null=True, upload_to='media/views'),
        ),
        migrations.AlterField(
            model_name='salepost',
            name='image2',
            field=models.ImageField(blank=True, default='media/views/default.jpg', null=True, upload_to='media/views'),
        ),
        migrations.AlterField(
            model_name='salepost',
            name='image3',
            field=models.ImageField(blank=True, default='media/views/default.jpg', null=True, upload_to='media/views'),
        ),
    ]
