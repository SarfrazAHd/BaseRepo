# Generated by Django 2.0.2 on 2020-02-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_delete_new_prod_arrival'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField()),
            ],
        ),
    ]