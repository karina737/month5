from rest_framework import serializers
from .models import Category, Product, Review


class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model=Category
        fields='name products_count'.split()
    def get_products_count(self, obj):
        return obj.product.count()
    
        
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='title category reviews '.split()
        depth=1
        
    def get_reviews(self, product):
        return product.reviews_name()
    
    
  
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='product text stars'.split()
class ProductReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'title category reviews rating'.split()
    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.count() == 0:
            return 0
        total = 0
        for review in reviews:
            total += review.stars
        return total / len(reviews)
   
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
