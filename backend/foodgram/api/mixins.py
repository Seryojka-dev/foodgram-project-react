from http import HTTPStatus
from django.shortcuts import get_object_or_404
from rest_framework import serializers, permissions, viewsets
from rest_framework.response import Response

from recipes.models import (
    Favorite, Recipe, ShoppingCart, Subscription,
)


class CommonSubscribedMixin(metaclass=serializers.SerializerMetaclass):
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        return Subscription.objects.filter(
                user=request.user, following__id=obj.id).exists()


class CommonRecipeMixin(metaclass=serializers.SerializerMetaclass):
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        return Favorite.objects.filter(
            user=request.user, recipe__id=obj.id).exists()

    def get_is_in_shopping_cart(self, obj):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        return ShoppingCart.objects.filter(
            user=request.user, recipe__id=obj.id).exists()


class CommonCountMixin(metaclass=serializers.SerializerMetaclass):
    recipes_count = serializers.SerializerMethodField()

    def get_recipes_count(self, obj):
        return Recipe.objects.filter(author__id=obj.id).count()


class BaseFavoriteCartViewSetMixin(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        recipe_id = int(self.kwargs['recipes_id'])
        recipe = get_object_or_404(Recipe, id=recipe_id)
        self.model.objects.create(
            user=request.user, recipe=recipe)
        return Response(HTTPStatus.CREATED)

    def delete(self, request, *args, **kwargs):
        recipe_id = self.kwargs['recipes_id']
        user_id = request.user.id
        get_object_or_404(
            self.model, user__id=user_id, recipe__id=recipe_id).delete()
        return Response(HTTPStatus.NO_CONTENT)
