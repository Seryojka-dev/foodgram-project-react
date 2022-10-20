from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
     CreateUserView, FavoriteViewSet, IngredientViewSet,
     RecipeViewSet, ShoppingCartViewSet,
     SubscribeViewSet, TagViewSet,
)

app_name = 'api'
router = DefaultRouter()

router.register('users', CreateUserView, basename='users')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    path('users/subscriptions/',
         SubscribeViewSet.as_view({'get': 'list'}), name='subscriptions'),
    path('users/<int:users_id>/subscribe/',
         SubscribeViewSet.as_view({'post': 'create',
                                   'delete': 'delete'}), name='subscribe'),
    path('recipes/<int:recipes_id>/shopping_cart/',
         ShoppingCartViewSet.as_view(
          {'post': 'create', 'delete': 'delete'}), name='shoppingcart'),
    path('recipes/<int:recipes_id>/favorite/',
         FavoriteViewSet.as_view({'post': 'create',
                                  'delete': 'delete'}), name='favorite'),
    path('recipes/download_shopping_cart/',
         RecipeViewSet.as_view(
          {'get': 'download_shoping_cart'}), name='download'),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
