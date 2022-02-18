# Generated by Django 4.0.2 on 2022-02-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostAPP', '0002_alter_modelpost_options_alter_modelpost_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Kategori İsmi')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
                'db_table': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='modelpost',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='İçerik'),
        ),
        migrations.AddField(
            model_name='modelpost',
            name='categories',
            field=models.ManyToManyField(to='PostAPP.ModelCategory', verbose_name='Kategoriler'),
        ),
    ]
