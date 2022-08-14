from django.urls import path
from .views import ListCategory,DetailCategory,ListBook,DetailBook,ListProduct,DetailProduct

urlpatterns = [
    path('', ListCategory.as_view(), name='category'),
    path('api/category/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    path('api/book', ListBook.as_view(),name='book'),
    path('api/book/<int:pk>/', DetailBook.as_view(), name='singlebook'),
    path('api/product', ListProduct.as_view(), name='product'),
    path('api/product/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
]