# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Recipe, RecipeDetail, SubRecipe


class RecipeFilter(django_filters.FilterSet):

    class Meta:
        model = Recipe
        fields = ('id', 'productForSale', 'recipes')


class RecipeDetailFilter(django_filters.FilterSet):

    class Meta:
        model = RecipeDetail
        fields = ('id', 'from_recipe', 'to_recipe', 'qty')


class SubRecipeFilter(django_filters.FilterSet):

    class Meta:
        model = SubRecipe
        fields = ('id', 'recipe', 'product', 'qty')
