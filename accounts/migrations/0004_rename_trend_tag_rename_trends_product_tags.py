# Generated by Django 4.1.1 on 2022-10-17 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trend',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='trends',
            new_name='tags',
        ),
    ]