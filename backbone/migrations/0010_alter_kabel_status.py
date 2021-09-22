# Generated by Django 3.2.4 on 2021-08-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backbone', '0009_alter_kabel_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kabel',
            name='status',
            field=models.CharField(choices=[('RI', 'Riješeno'), ('ZA', 'Zastoj'), ('IZ', 'U izvođenju')], default='IZ', max_length=20),
        ),
    ]
