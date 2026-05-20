from django.db import models

# Категория (Category)
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Продукт (Product)
class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.title


# Отзыв (Review)
class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]  # ⭐ от 1 до 5
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        return self.text