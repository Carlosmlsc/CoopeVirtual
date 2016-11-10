# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Recipe, SubRecipe, RecipeDetail
from .filters import RecipeFilter, SubRecipeFilter, RecipeDetailFilter


# API

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'productForSale', 'recipes')


class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    lookup_field = 'id'
    filter_class = RecipeFilter


class RecipeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeDetail
        fields = ('id', 'from_recipe', 'to_recipe', 'qty')


class RecipeDetailViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeDetailSerializer
    queryset = RecipeDetail.objects.all()
    lookup_field = 'id'
    filter_class = RecipeDetailFilter


class SubRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubRecipe
        fields = ('id', 'productForSale', 'recipes')


class SubRecipeViewSet(viewsets.ModelViewSet):

    serializer_class = SubRecipeSerializer
    queryset = SubRecipe.objects.all()
    lookup_field = 'id'
    filter_class = SubRecipeFilter
