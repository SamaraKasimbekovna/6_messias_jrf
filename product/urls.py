from django.urls import path
from . import views

urlpatterns = [
    # CATEGORY
    path('categories/', views.category_list),
    path('categories/<int:id>/', views.category_detail),

    # PRODUCT
    path('product/', views.product_list),
    path('product/<int:id>/', views.product_detail),

    # REVIEW
    path('reviews/', views.review_list),
    path('reviews/<int:id>/', views.review_detail),
]