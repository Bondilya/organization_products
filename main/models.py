from decimal import Decimal

from django.db import models


class District(models.Model):
    name = models.CharField(max_length=256, db_index=True)

    def __str__(self):
        return self.name


class OrganizationNetwork(models.Model):
    name = models.CharField(max_length=256, db_index=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    network = models.ForeignKey(OrganizationNetwork, on_delete=models.PROTECT)
    districts = models.ManyToManyField(District)
    products = models.ManyToManyField('Product', through='OrganizationProduct')

    def get_districts(self):
        return ', '.join((district.name for district in self.districts.all()))
    get_districts.short_description = 'Districts'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class OrganizationProduct(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))

    def __str__(self):
        return f'Product "{self.product}" in {self.organization} with price: {self.price}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['organization', 'product'], name='organization_product'),
        ]
