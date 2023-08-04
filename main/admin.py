from django.contrib import admin

from main.models import (Category, District, Organization, OrganizationNetwork,
                         OrganizationProduct, Product)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class OrganizationNetworkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class OrganizationProductInline(admin.TabularInline):
    model = OrganizationProduct
    extra = 1


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_districts', 'network')
    search_fields = ('name', 'network__name', 'districts__name')
    list_filter = ('network', 'districts')
    fields = ('name', 'districts', 'network',)
    inlines = [OrganizationProductInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('category', )
    search_fields = ('name', 'category__name')


class OrganizationProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'organization')
    list_filter = ('organization', )
    search_fields = ('product', 'price', 'organization')


admin.site.register(District, DistrictAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrganizationProduct, OrganizationProductAdmin)
admin.site.register(OrganizationNetwork, OrganizationNetworkAdmin)
admin.site.register(Organization, OrganizationAdmin)
