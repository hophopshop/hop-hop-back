# Generated by Django 5.0.6 on 2024-09-14 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0012_alter_product_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["-id"],
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.AlterModelOptions(
            name="productimage",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="shop.category",
            ),
        ),
    ]