# Generated by Django 3.0.5 on 2020-04-12 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20200412_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_number',
            new_name='orderCount',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='totalOrder',
            new_name='totalOrderCost',
        ),
    ]
