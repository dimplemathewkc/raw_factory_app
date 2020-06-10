# Generated by Django 3.0.7 on 2020-06-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='quantity_type',
            field=models.CharField(choices=[('oz', 'OZ'), ('l', 'L'), ('ml', 'ML'), ('kg', 'KG')], default='oz', max_length=4),
        ),
    ]