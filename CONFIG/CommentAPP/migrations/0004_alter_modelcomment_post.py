# Generated by Django 4.0.2 on 2022-02-25 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostAPP', '0002_initial'),
        ('CommentAPP', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='PostAPP.modelpost', verbose_name='Post'),
        ),
    ]
