# Generated by Django 3.2.4 on 2021-07-26 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backbone', '0002_auto_20210726_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaposlenik',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='zaposlenik', to=settings.AUTH_USER_MODEL),
        ),
    ]
