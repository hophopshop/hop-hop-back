# Generated by Django 5.0.6 on 2024-10-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0016_alter_productimage_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={"ordering": ["order", "-id"]},
        ),
        migrations.AddField(
            model_name="productimage",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
