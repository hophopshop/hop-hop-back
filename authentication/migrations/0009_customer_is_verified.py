# Generated by Django 5.0.6 on 2024-11-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0008_alter_customer_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="is_verified",
            field=models.BooleanField(default=False),
        ),
    ]