from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    CategoryValidateSerializer,
    ProductValidateSerializer,
    ReviewValidateSerializer
)
from .permissions import IsModerator
from common.validators import validate_user_age


# ================= CATEGORY =================

@api_view(['GET', 'POST'])
@permission_classes([IsModerator])
def category_list(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)

    if request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = Category.objects.create(
            name=serializer.validated_data['name']
        )

        return Response(
            CategorySerializer(category).data,
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsModerator])
def category_detail(request, id):

    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(CategorySerializer(category).data)

    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category.name = serializer.validated_data['name']
        category.save()

        return Response(CategorySerializer(category).data)


# ================= PRODUCT =================

@api_view(['GET', 'POST'])
@permission_classes([IsModerator])
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)

    if request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = Product.objects.create(
            title=serializer.validated_data['title'],
            category_id=serializer.validated_data['category_id']
        )

        return Response(
            ProductSerializer(product).data,
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsModerator])
def product_detail(request, id):

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(ProductSerializer(product).data)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product.title = serializer.validated_data['title']
        product.category_id = serializer.validated_data['category_id']
        product.save()

        return Response(ProductSerializer(product).data)


# ================= REVIEW =================

@api_view(['GET', 'POST'])
@permission_classes([IsModerator])
def review_list(request):

    if request.method == 'GET':
        reviews = Review.objects.all()
        return Response(ReviewSerializer(reviews, many=True).data)

    if request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review = Review.objects.create(
            text=serializer.validated_data['text'],
            stars=serializer.validated_data['stars'],
            product_id=serializer.validated_data['product_id']
        )

        return Response(
            ReviewSerializer(review).data,
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsModerator])
def review_detail(request, id):

    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(ReviewSerializer(review).data)

    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data['text']
        review.stars = serializer.validated_data['stars']
        review.product_id = serializer.validated_data['product_id']
        review.save()

        return Response(ReviewSerializer(review).data)