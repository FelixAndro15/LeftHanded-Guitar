# Generated by Django 5.0.3 on 2024-05-23 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_orderitem_date_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='date_ordered',
        ),
    ]
