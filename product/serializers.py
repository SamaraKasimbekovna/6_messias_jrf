from rest_framework import serializers
from .models import Product, Category, Review


# ================= REVIEW =================

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars']


# ================= PRODUCT =================

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'reviews', 'rating']

    def get_rating(self, obj):
        reviews = obj.reviews.all()

        if reviews.exists():
            return sum(r.stars for r in reviews) / reviews.count()

        return 0


# ================= CATEGORY =================

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, obj):
        return obj.products.count()


# ================= VALIDATION =================

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=2, max_length=100)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=2, max_length=255)
    category_id = serializers.IntegerField()

    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Category does not exist!")
        return value


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, min_length=2)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product does not exist!")
        return value