# Generated by Django 4.2.7 on 2023-12-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_name_product_name_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('Digital', 'Digital'), ('kitchen', 'kitchen'), ('Clothes', 'Clothes'), ('Health', 'Health')], default='Digital', max_length=15),
        ),
    ]
