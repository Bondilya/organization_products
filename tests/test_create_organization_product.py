import pytest
from rest_framework import status

from main.models import OrganizationProduct


@pytest.mark.django_db
def test_create_organization_product(organization_product, authenticated_client):
    response = authenticated_client.post('/api/products/', organization_product, format='json')

    assert response.status_code == status.HTTP_201_CREATED

    created_organization_product = OrganizationProduct.objects.first()

    assert created_organization_product is not None
    assert created_organization_product.product.name == organization_product['product']['name']
    assert created_organization_product.product.category.pk == organization_product['product']['category']
    assert created_organization_product.organization.pk == organization_product['organization']


@pytest.mark.django_db
def test_raise_conflict_on_create_dublicate_organization_product(
    created_organization_product,
    organization_product,
    authenticated_client,
):
    response = authenticated_client.post('/api/products/', organization_product, format='json')
    assert response.status_code == status.HTTP_409_CONFLICT
