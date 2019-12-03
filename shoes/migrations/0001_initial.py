# Generated by Django 2.2.8 on 2019-12-03 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('url', models.URLField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('RED', 'Red'), ('ORANGE', 'Orange'), ('YELLOW', 'Yellow'), ('GREEN', 'Green'), ('BLUE', 'Blue'), ('INDIGO', 'Indigo'), ('VIOLET', 'Violet'), ('WWHITE', 'White'), ('BLACK', 'Black')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('SNEAKER', 'Sneaker'), ('BOOT', 'Boot'), ('SANDAL', 'Sandal'), ('DRESS', 'Dress'), ('OTHER', 'Other')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('brand_name', models.CharField(max_length=25)),
                ('material', models.CharField(max_length=25)),
                ('fasten_type', models.CharField(max_length=25)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.ShoeType')),
            ],
        ),
    ]