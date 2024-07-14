from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')
# router.register('cart', views.CollectionViewSet, basename='cart')


products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls
# urlpatterns = [
#     path("products/", views.ProductList.as_view()),
#     path("products/<int:pk>/", views.ProductDetail.as_view()),
#     path("collections/", views.CollectionList.as_view()),
#     path("collections/<int:pk>/", views.CollectionDetail.as_view(), name='collection-detail'),
# ]