# Generated by Django 2.1.4 on 2019-01-09 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_auto_20190102_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='责任人'),
        ),
    ]