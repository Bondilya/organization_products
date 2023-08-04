from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from main.models import District, Organization, OrganizationProduct, Product
from main.serializers import (OrganizationDetailSerializer,
                              OrganizationProductCreateSerializer,
                              OrganizationProductSerializer,
                              OrganizationSerializer, ProductDetailSerializer)


class OrganizationList(generics.ListAPIView):
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        district = get_object_or_404(District, pk=self.kwargs['district_id'])
        queryset = Organization.objects.filter(districts=district)
        return queryset


class OrganizationDetail(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationDetailSerializer
    lookup_field = 'pk'


class OrganizationProductList(generics.ListAPIView):
    serializer_class = OrganizationProductSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['product__name', 'product__category__name']

    def get_queryset(self):
        organization = get_object_or_404(Organization, pk=self.kwargs['organization_id'])
        queryset = OrganizationProduct.objects.filter(organization=organization)

        return queryset


class CreateProduct(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = OrganizationProduct.objects.all()
    serializer_class = OrganizationProductCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })
