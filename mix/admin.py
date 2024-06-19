from django.contrib import admin
from mix.models import *


@admin.register(MixCategory)
class MixCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Mix)
class MixAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)


@admin.register(MixTag)
class MixTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ('id', 'mix', 'tobacco', 'percentage')
    list_filter = ('percentage',)
