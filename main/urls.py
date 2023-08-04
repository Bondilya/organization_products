from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from main.views import (CreateProduct, OrganizationDetail, OrganizationList,
                        OrganizationProductList, ProductDetail)

urlpatterns = [
    path('organizations/<int:district_id>/', OrganizationList.as_view()),
    path('organizations-product/<int:organization_id>/', OrganizationProductList.as_view()),
    path('organizations/detail/<int:pk>/', OrganizationDetail.as_view()),
    path('products/', CreateProduct.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
