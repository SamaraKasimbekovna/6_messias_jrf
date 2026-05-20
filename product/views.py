from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    CategoryValidateSerializer,
    ProductSerializer,
    ProductValidateSerializer,
    ReviewSerializer,
    ReviewValidateSerializer
)

# CATEGORY

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorySerializer
        return CategoryValidateSerializer


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorySerializer
        return CategoryValidateSerializer

# PRODUCT


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductValidateSerializer


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductValidateSerializer


# REVIEW

class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewSerializer
        return ReviewValidateSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewSerializer
        return ReviewValidateSerializer