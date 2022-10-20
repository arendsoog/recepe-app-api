"""
Serializers for recipe APIs
"""

from rest_framework import serializers

from core.models import (
    Recipe,
    Tag
)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serializer for recipe detail"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializer fro tags"""

    class Meta:
        model = Tag
        fiels = ['id', 'name']
        read_only_fields = ['id']
