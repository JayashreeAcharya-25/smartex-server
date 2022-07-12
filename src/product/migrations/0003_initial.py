# Generated by Django 4.0.5 on 2022-07-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_slno', models.CharField(max_length=150)),
                ('pro_code', models.CharField(max_length=150)),
                ('pro_name', models.CharField(max_length=200)),
                ('pro_image', models.ImageField(upload_to='products/')),
                ('pro_desc', models.CharField(max_length=3000)),
                ('pro_brand', models.CharField(max_length=150)),
                ('pro_category', models.CharField(max_length=150)),
                ('pro_color', models.CharField(max_length=500)),
                ('pro_sgst', models.DecimalField(decimal_places=0, max_digits=16)),
                ('pro_cgst', models.DecimalField(decimal_places=0, max_digits=16)),
                ('pro_price', models.DecimalField(decimal_places=0, max_digits=16)),
                ('uid', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
    ]
