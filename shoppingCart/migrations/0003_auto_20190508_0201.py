# Generated by Django 2.2 on 2019-05-08 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='modelNUmber',
            new_name='modelNumber',
        ),
        migrations.AddField(
            model_name='customer',
            name='customerID',
            field=models.CharField(default='XXXX', max_length=20),
            preserve_default=False,
        ),
    ]
