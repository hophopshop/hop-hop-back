# Generated by Django 5.0.6 on 2024-09-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0004_order_payment_id_order_payment_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="paid",
        ),
        migrations.RemoveField(
            model_name="order",
            name="status",
        ),
        migrations.AddField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("Pending", "Status Pending"),
                    ("In Progress", "Status In Progress"),
                    ("In Transit", "Status In Transit"),
                    ("Delivered", "Status Delivered"),
                    ("Canceled", "Status Canceled"),
                ],
                default="Pending",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("Pending", "Status Pending"),
                    ("Paid", "Status Paid"),
                    ("Canceled", "Status Canceled"),
                    ("Failed", "Status Failed"),
                ],
                default="Pending",
                max_length=50,
            ),
        ),
    ]