# Generated by Django 5.0.6 on 2024-10-13 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0013_alter_order_order_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="shipping_city",
        ),
        migrations.RemoveField(
            model_name="order",
            name="shipping_country",
        ),
    ]
