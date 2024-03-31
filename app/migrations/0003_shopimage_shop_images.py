# Generated by Django 4.2.11 on 2024-03-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_category_options_alter_city_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shop/images/')),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='images',
            field=models.ManyToManyField(to='app.shopimage'),
        ),
    ]