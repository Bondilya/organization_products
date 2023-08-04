import json

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_organization_products(created_organization_product, authenticated_client):
    response = authenticated_client.get(f'/api/organizations-product/{created_organization_product.organization.pk}/')

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_return_404_on_get_organization_products_by_not_exists_organization(
    created_organization_product,
    authenticated_client,
):
    response = authenticated_client.get(f'/api/organizations-product/{created_organization_product.organization.pk-1}/')

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_organization_products_search_by_product_name_working(
    organization_product,
    created_organization_product,
    authenticated_client,
):
    incomplete_product_name = created_organization_product.product.name[:3]
    response = authenticated_client.get(
        f'/api/organizations-product/{created_organization_product.organization.pk}/',
        params={'search': incomplete_product_name},
    )
    response_data = json.loads(response.content)

    assert response_data[0]['product']['name'] == organization_product['product']['name']


@pytest.mark.django_db
def test_get_organization_products_search_by_product_name_working(
        organization_product,
        created_organization_product,
        authenticated_client,
):
    incomplete_category_name = created_organization_product.product.category.name[:3]
    response = authenticated_client.get(
        f'/api/organizations-product/{created_organization_product.organization.pk}/',
        params={'search': incomplete_category_name},
    )
    response_data = json.loads(response.content)

    assert response_data[0]['product']['category'] == organization_product['product']['category']
