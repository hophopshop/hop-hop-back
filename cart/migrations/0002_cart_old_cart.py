# Generated by Django 4.2.13 on 2024-06-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="old_cart",
            field=models.TextField(blank=True, null=True),
        ),
    ]
