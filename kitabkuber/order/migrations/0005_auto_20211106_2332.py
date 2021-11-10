# Generated by Django 3.2.8 on 2021-11-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20211106_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid_amount',
        ),
        migrations.AddField(
            model_name='order',
            name='book_name',
            field=models.CharField(default=' ', max_length=20000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='deposit',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='mrp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='rent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]