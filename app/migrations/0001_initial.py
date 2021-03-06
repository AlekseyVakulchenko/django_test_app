# Generated by Django 3.1.7 on 2021-03-01 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField(max_length=255)),
                ('last_name', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='CustomProduct',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Custom product',
                'verbose_name_plural': 'Custom products',
            },
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('email_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email_address', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='NonCustomProduct',
            fields=[
                ('p_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Non custom product',
                'verbose_name_plural': 'Non custom products',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('status_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Order status',
                'verbose_name_plural': 'Order status',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_number', models.TextField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app.customer')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app.orderstatus')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_order_items', to='app.orders')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_product_order_item', to='app.customproduct')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order_item', to='app.customproduct')),
            ],
            options={
                'verbose_name': 'Order item',
                'verbose_name_plural': 'Order items',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='app.emails'),
        ),
    ]
