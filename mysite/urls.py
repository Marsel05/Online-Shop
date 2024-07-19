from django.contrib.auth.urls import path
from .views import *

urlpatterns = [
    path('userprofile/', UserProfileView.as_view({"get": 'list', 'post': 'create'}), name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile_detail'),

    path('category/', CategoryView.as_view({"get": 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),
    path('product/', ProductView.as_view({"get": 'list', 'post': 'create'}), name='product_list'),
    path('product/<int:pk>/', ProductView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),
    path('supplier/', SupplierView.as_view({"get": 'list', 'post': 'create'}), name='supplier_list'),
    path('supplier/<int:pk>/', SupplierView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='supplier_detail'),
    path('order/', OrderView.as_view({"get": 'list', 'post': 'create'}), name='order_list'),
    path('order/<int:pk>/', OrderView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),
    path('order_item/', OrderItemView.as_view({"get": 'list', 'post': 'create'}), name='order_item_list'),
    path('order_item/<int:pk>/', OrderItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_item_detail'),
    path('payment/', PaymentView.as_view({"get": 'list', 'post': 'create'}), name='payment_list'),
    path('payment/<int:pk>/', PaymentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='payment_detail'),
    path('review/', ReviewView.as_view({"get": 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),

]