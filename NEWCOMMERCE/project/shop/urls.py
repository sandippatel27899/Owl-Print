from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="products"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    # path("profile/<int:pk>/", views.ProfileDetailView.as_view(), name="profile-detail"),
    path('search/', views.search, name='search'),
    path('filter/', views.filter, name='filter'),

] + [
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('orders/', views.orders, name='orders'),
    path('profile/', views.profile, name='profile'),
]
