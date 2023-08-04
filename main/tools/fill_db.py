import random

from faker import Faker

from main.models import District, Organization, OrganizationNetwork, OrganizationProduct, Category, Product

faker = Faker()

DISTRICT_COUNT = 2
ORGANIZATION_NETWORK_COUNT = 3
ORGANIZATION_COUNT = 10
CATEGORY_COUNT = 20
PRODUCT_COUNT = 100


district_objects = [District(name=faker.state()) for _ in range(DISTRICT_COUNT)]
District.objects.bulk_create(district_objects)

organization_network_objects = [OrganizationNetwork(name=faker.company()) for _ in range(ORGANIZATION_NETWORK_COUNT)]
OrganizationNetwork.objects.bulk_create(organization_network_objects)

category_objects = [Category(name=faker.word()) for _ in range(CATEGORY_COUNT)]
Category.objects.bulk_create(category_objects)

product_objects = [
    Product(
        name=faker.word(), category=random.choice(category_objects)
    ) for _ in range(PRODUCT_COUNT)
]
Product.objects.bulk_create(product_objects)

organization_objects = [
    Organization(
        name=faker.company(),
        network=random.choice(organization_network_objects),
    ) for _ in range(ORGANIZATION_COUNT)
]
Organization.objects.bulk_create(organization_objects)

for organization_object in organization_objects:
    organization_object.districts.add(*set(random.choices(district_objects, k=random.randint(1, DISTRICT_COUNT))))
    organization_object.products.add(*set(random.choices(product_objects, k=random.randint(1, DISTRICT_COUNT))))


organization_product_objects = (
    OrganizationProduct(
        product=random.choice(product_objects),
        organization=random.choice(organization_objects),
        price=faker.pydecimal(min_value=1, max_value=10_000, positive=True, right_digits=2),
    ) for _ in range(ORGANIZATION_COUNT * PRODUCT_COUNT)
)
# TODO make records without conflicts
OrganizationProduct.objects.bulk_create(
    organization_product_objects,
    ignore_conflicts=True,
)
