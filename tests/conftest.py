import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

import organizations.settings
from main.models import (Category, District, Organization, OrganizationNetwork,
                         OrganizationProduct, Product)

ADMIN_PASSWORD = 'admin_password_321'


# fixtures
# @pytest.fixture(autouse=True)
# def patch_db(monkeypatch):
#     local_db_database_setting = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': organizations.settings.BASE_DIR / 'db.sqlite3',
#         }
#     }
#     monkeypatch.setattr(organizations.settings, 'DATABASES', local_db_database_setting)


@pytest.mark.django_db
@pytest.fixture
def authenticated_client(admin_user):
    client = APIClient()
    response = client.post('/api/token/', {'username': admin_user.username, 'password': ADMIN_PASSWORD})
    response_data = json.loads(response.content)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response_data['access'])

    yield client


@pytest.mark.django_db
@pytest.fixture
def admin_user():
    return User.objects.create_user(username='admin', password=ADMIN_PASSWORD)


@pytest.mark.django_db
@pytest.fixture
def created_category():
    return Category.objects.create(name='Category')


@pytest.mark.django_db
@pytest.fixture
def created_district():
    return District.objects.create(name='District')


@pytest.mark.django_db
@pytest.fixture
def created_organization(created_district, created_organization_network):
    organization = Organization.objects.create(name='SomeOrganization', network=created_organization_network)
    organization.districts.add(created_district)
    return organization


@pytest.mark.django_db
@pytest.fixture
def created_organization_network():
    return OrganizationNetwork.objects.create(name='SomeNetwork')


@pytest.mark.django_db
@pytest.fixture
def created_organization_product(organization_product, created_organization, created_product):
    return OrganizationProduct.objects.create(
        product=created_product,
        organization=created_organization,
        price=organization_product['price'],
    )


@pytest.mark.django_db
@pytest.fixture
def created_product(created_category, product):
    return Product.objects.create(category=created_category, name=product['name'])


@pytest.fixture
def organization_product(created_category, created_organization, product):
    yield {
        'product': product,
        'price': 1500,
        'organization': created_organization.pk,
    }


@pytest.fixture
def product(created_category):
    yield {
        'name': 'T-Shirt',
        'category': created_category.pk,
    }
