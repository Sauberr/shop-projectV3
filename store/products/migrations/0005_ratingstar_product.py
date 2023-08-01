# Generated by Django 4.2.3 on 2023-07-28 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingstar',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='products.product'),
        ),
    ]
