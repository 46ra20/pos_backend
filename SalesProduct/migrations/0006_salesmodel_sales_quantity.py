# Generated by Django 5.1 on 2024-09-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesProduct', '0005_remove_salesmodel_sales_item_salesmodel_sales_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesmodel',
            name='sales_quantity',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
    ]
