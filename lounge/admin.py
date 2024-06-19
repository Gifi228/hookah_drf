from django.contrib import admin

from lounge.models import *


@admin.register(Lounge)
class LoungeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lounge')


@admin.register(LoungeImages)
class LoungeImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')


@admin.register(Metro)
class MetroAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
