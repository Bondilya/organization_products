import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_product_detail_working(created_product, authenticated_client):
    response = authenticated_client.get(f'/api/products/{created_product.pk}/')

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_return_404_on_get_organization_by_not_exists_district(created_product, authenticated_client):
    response = authenticated_client.get(f'/api/organizations/{created_product.pk - 1}/')

    assert response.status_code == status.HTTP_404_NOT_FOUND
