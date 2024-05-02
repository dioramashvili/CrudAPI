from rest_framework import generics
from rest_api.models import Product, Category
from rest_framework.permissions import IsAdminUser
from rest_api.serializers import (ProductSerializer,
                                  CategorySerializer,
                                  ProductListSerializer,
                                  CategoryListSerializer)


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAdminUser]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAdminUser]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
