from django.urls import path
from . import views

urlpatterns=[
    path('new/', views.ProductCreateAPIView.as_view(), name='new-product'),
    path('list/', views.ProductListAPIView.as_view(), name='product-list'),
    path('<str:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('<str:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update'),
    path('<str:pk>/destroy/', views.ProductDestroyAPIView.as_view(), name='product-destroy'),
]