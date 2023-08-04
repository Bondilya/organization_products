from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from main.models import (Category, District, Organization, OrganizationNetwork,
                         OrganizationProduct, Product)


class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'This object already exist'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrganizationNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationNetwork
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ['products', ]


class OrganizationProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=False)

    class Meta:
        model = OrganizationProduct
        fields = ['product', 'price']


class OrganizationProductCreateSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = OrganizationProduct
        fields = '__all__'

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product, _ = Product.objects.get_or_create(**product_data)
        organization_product, is_created = OrganizationProduct.objects.get_or_create(product=product, **validated_data)

        if not is_created:
            raise Conflict

        return organization_product


class OrganizationDetailSerializer(serializers.ModelSerializer):
    network = OrganizationNetworkSerializer(read_only=True, many=False)
    districts = DistrictSerializer(read_only=True, many=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Organization
        fields = ['name', 'network', 'districts', 'products']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)

    class Meta:
        model = Product
        fields = ['name', 'category']
