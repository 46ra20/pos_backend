# Generated by Django 4.2.14 on 2024-08-26 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='./Image/Product'),
            preserve_default=False,
        ),
    ]
