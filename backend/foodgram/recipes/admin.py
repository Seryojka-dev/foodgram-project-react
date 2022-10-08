from django.contrib import admin
from users.models import User

from .models import (
    Favorite, Ingredient, IngredientAmount, Recipe,
    ShoppingCart, Subscription, Tag, TagRecipe,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id')
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'
    list_filter = ('username', 'email')


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 0


class TagRecipeInline(admin.TabularInline):
    model = TagRecipe
    extra = 0


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    empty_value_display = '-пусто-'
    list_filter = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', )
    empty_value_display = '-пусто-'
    list_filter = ('name',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'id')
    search_fields = ('user', )
    empty_value_display = '-пусто-'
    list_filter = ('user',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user', )
    empty_value_display = '-пусто-'
    list_filter = ('user',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountInline, TagRecipeInline,)
    list_display = ('name', 'author', 'cooking_time',
                    'id', 'count_favorite', 'pub_date')
    search_fields = ('name', 'author', 'tags')
    empty_value_display = '-пусто-'
    list_filter = ('name', 'author', 'tags')

    def count_favorite(self, obj):
        return Favorite.objects.filter(recipe=obj).count()

    count_favorite.short_description = 'Число добавлений в избранное'


@admin.register(Subscription)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user', )
    empty_value_display = '-пусто-'
    list_filter = ('user',)
