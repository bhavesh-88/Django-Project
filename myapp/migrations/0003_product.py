# Generated by Django 4.1.6 on 2023-02-18 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('men', 'men'), ('women', 'women'), ('kid', 'kid')], max_length=100)),
                ('product_price', models.PositiveIntegerField()),
                ('product_desc', models.CharField(max_length=100)),
                ('product_size', models.CharField(choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=100)),
                ('product_image', models.ImageField(upload_to='product_pic/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
