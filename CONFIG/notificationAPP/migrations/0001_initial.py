# Generated by Django 4.0.2 on 2022-02-19 16:45

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
            name='ModelNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250, verbose_name='Bildirim İçeriği')),
                ('isRead', models.BooleanField(default=False, verbose_name='Okundu mu')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('kind', models.CharField(choices=[('1', 'Takip'), ('2', 'Yorum'), ('3', 'Beğeni')], max_length=7)),
                ('receiverUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifs', to=settings.AUTH_USER_MODEL, verbose_name='Alan Kullanıcı')),
                ('senderUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Gönderen Kullanıcı')),
            ],
        ),
    ]
