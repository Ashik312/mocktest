# Generated by Django 3.1.5 on 2023-07-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_desc', models.CharField(max_length=200)),
                ('product_img', models.ImageField(upload_to='proimg')),
            ],
        ),
    ]
