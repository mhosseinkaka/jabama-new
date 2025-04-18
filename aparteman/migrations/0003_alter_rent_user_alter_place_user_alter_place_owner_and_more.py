# Generated by Django 5.1.6 on 2025-04-11 08:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparteman', '0002_rent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_place_aparteman_rent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_aparteman', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_aparteman', to='aparteman.owner'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_place_aparteman_rent', to='aparteman.owner'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_aparteman_rent', to='aparteman.place'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
