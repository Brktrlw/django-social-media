# Generated by Django 4.0.2 on 2022-02-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeluser',
            name='profilePhoto',
            field=models.ImageField(null=True, upload_to='ProfilePhotos'),
        ),
    ]
