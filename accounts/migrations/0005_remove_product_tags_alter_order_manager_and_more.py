# Generated by Django 4.1.2 on 2022-10-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_trend_tag_rename_trends_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='order',
            name='manager',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
