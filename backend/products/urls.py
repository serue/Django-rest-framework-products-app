from django.urls import path
from . import views

urlpatterns=[
    path('new/', views.ProductCreateAPIView.as_view()),
    path('list/', views.ProductListAPIView.as_view()),
    path('<str:pk>/', views.ProductDetailAPIView.as_view()),
     path('<str:pk>/update/', views.ProductUpdateAPIView.as_view()),
      path('<str:pk>/destroy/', views.ProductDestroyAPIView.as_view()),
]