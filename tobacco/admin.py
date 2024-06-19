from django.contrib import admin
from tobacco.models import *


class StrengthChoicesTobaccoInline(admin.TabularInline):
    model = Tobacco
    extra = 'hard'


class TypeChoicesTobaccoInline(admin.TabularInline):
    model = Tobacco
    extra = 'mint'


@admin.register(Tobacco)
class TabaccoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TabaccoTag)
class TabaccoTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(PreMethod)
class PreMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(TobaccoImages)
class TobaccoImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'tobacco')




