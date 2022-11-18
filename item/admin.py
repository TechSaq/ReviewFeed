from django.contrib import admin

from .models import (
    Category,
    Item,
    ItemSpecificationValue,
    ItemType,
    Review,
    ItemSpecification,
)


admin.site.register(Category)


# class EventTypeAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}


# class ItemAdmin(admin.ModelAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'user',  'description',)


class ItemSpecificationInline(admin.TabularInline):
    model = ItemSpecification


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    inlines = [ItemSpecificationInline]
    prepopulated_fields = {"slug": ("name",)}


class ItemSpecificationValueInline(admin.TabularInline):
    model = ItemSpecificationValue


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemSpecificationValueInline]
    list_display = ('title', 'item_type',)
    prepopulated_fields = {"slug": ("title",)}
