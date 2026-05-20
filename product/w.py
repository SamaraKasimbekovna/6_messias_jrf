# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
#
# from .models import Category, Product, Review
#
# from .serializers import (
#     CategorySerializer,
#     ProductSerializer,
#     ReviewSerializer,
#
#     CategoryValidateSerializer,
#     ProductValidateSerializer,
#     ReviewValidateSerializer
# )
# # ================= CATEGORY =================
#
# @api_view(['GET', 'POST'])
# def category_list(request):
#
#     if request.method == 'GET':
#
#         categories = Category.objects.all()
#
#         data = CategorySerializer(
#             categories,
#             many=True
#         ).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#
#     elif request.method == 'POST':
#
#         serializer = CategoryValidateSerializer(
#             data=request.data
#         )
#
#         if not serializer.is_valid():
#
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         name = serializer.validated_data.get('name')
#
#         category = Category.objects.create(
#             name=name
#         )
#
#         return Response(
#             data=CategorySerializer(category).data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail(request, id):
#
#     try:
#         category = Category.objects.get(id=id)
#
#     except Category.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND
#         )
#
#     if request.method == 'GET':
#
#         data = CategorySerializer(category).data
#
#         return Response(data=data)
#
#     elif request.method == 'DELETE':
#
#         category.delete()
#
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
#
#     elif request.method == 'PUT':
#
#         serializer = CategoryValidateSerializer(
#             data=request.data
#         )
#
#         serializer.is_valid(raise_exception=True)
#
#         category.name = serializer.validated_data.get('name')
#
#         category.save()
#
#         return Response(
#             data=CategorySerializer(category).data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# # ================= PRODUCT =================
#
# @api_view(['GET', 'POST'])
# def product_list(request):
#     print(request.user)
#
#     if request.method == 'GET':
#
#         products = Product.objects.all()
#
#         data = ProductSerializer(
#             products,
#             many=True
#         ).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#
#     elif request.method == 'POST':
#
#         serializer = ProductValidateSerializer(
#             data=request.data
#         )
#
#         if not serializer.is_valid():
#
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         title = serializer.validated_data.get('title')
#         category_id = serializer.validated_data.get('category_id')
#
#         product = Product.objects.create(
#             title=title,
#             category_id=category_id
#         )
#
#         return Response(
#             data=ProductSerializer(product).data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, id):
#
#     try:
#         product = Product.objects.get(id=id)
#
#     except Product.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND
#         )
#
#     if request.method == 'GET':
#
#         data = ProductSerializer(product).data
#
#         return Response(data=data)
#
#     elif request.method == 'DELETE':
#
#         product.delete()
#
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
#
#     elif request.method == 'PUT':
#
#         serializer = ProductValidateSerializer(
#             data=request.data
#         )
#
#         serializer.is_valid(raise_exception=True)
#
#         product.title = serializer.validated_data.get('title')
#
#         product.category_id = serializer.validated_data.get(
#             'category_id'
#         )
#
#         product.save()
#
#         return Response(
#             data=ProductSerializer(product).data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# # ================= REVIEW =================
#
# @api_view(['GET', 'POST'])
# def review_list(request):
#
#     if request.method == 'GET':
#
#         reviews = Review.objects.all()
#
#         data = ReviewSerializer(
#             reviews,
#             many=True
#         ).data
#
#         return Response(
#             data=data,
#             status=status.HTTP_200_OK
#         )
#
#     elif request.method == 'POST':
#
#         serializer = ReviewValidateSerializer(
#             data=request.data
#         )
#
#         if not serializer.is_valid():
#
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         text = serializer.validated_data.get('text')
#         stars = serializer.validated_data.get('stars')
#         product_id = serializer.validated_data.get('product_id')
#
#         review = Review.objects.create(
#             text=text,
#             stars=stars,
#             product_id=product_id
#         )
#
#         return Response(
#             data=ReviewSerializer(review).data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail(request, id):
#
#     try:
#         review = Review.objects.get(id=id)
#
#     except Review.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND
#         )
#
#     if request.method == 'GET':
#
#         data = ReviewSerializer(review).data
#
#         return Response(data=data)
#
#     elif request.method == 'DELETE':
#
#         review.delete()
#
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
#
#     elif request.method == 'PUT':
#
#         serializer = ReviewValidateSerializer(
#             data=request.data
#         )
#
#         serializer.is_valid(raise_exception=True)
#
#         review.text = serializer.validated_data.get('text')
#
#         review.stars = serializer.validated_data.get('stars')
#
#         review.product_id = serializer.validated_data.get(
#             'product_id'
#         )
#
#         review.save()
#
#         return Response(
#             data=ReviewSerializer(review).data,
#             status=status.HTTP_201_CREATED
#         )