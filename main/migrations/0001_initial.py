# Generated by Django 4.2.4 on 2023-08-03 22:00

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
                ('districts', models.ManyToManyField(to='main.district')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.organization')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.organizationnetwork'),
        ),
        migrations.AddField(
            model_name='organization',
            name='products',
            field=models.ManyToManyField(through='main.OrganizationProduct', to='main.product'),
        ),
        migrations.AddConstraint(
            model_name='organizationproduct',
            constraint=models.UniqueConstraint(fields=('organization', 'product'), name='organization_product'),
        ),
    ]
