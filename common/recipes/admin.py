# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Recipe, SubRecipe, RecipeDetail


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('id', 'productForSale')

    search_fields = ('id', 'productForSale')

    filter_horizontal = ('recipes',)


@admin.register(SubRecipe)
class SubRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'product', 'qty')

    search_fields = ('id', 'recipe', 'product', 'qty')


@admin.register(RecipeDetail)
class RecipeDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_recipe', 'to_recipe', 'qty')

    search_fields = ('id', 'from_recipe', 'to_recipe', 'qty')
