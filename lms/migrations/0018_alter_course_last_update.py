# Generated by Django 4.2.3 on 2023-08-04 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0017_remove_subscription_last_update_course_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время последнего обновления'),
        ),
    ]
