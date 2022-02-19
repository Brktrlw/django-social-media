# Generated by Django 4.0.2 on 2022-02-19 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LikeAPP', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CommentAPP', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpostlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AddField(
            model_name='modelcommentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='CommentAPP.modelcomment', verbose_name='Yorum'),
        ),
        migrations.AddField(
            model_name='modelcommentlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]
