
from rest_framework.decorators import api_view as shop_api
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import (CategoryListSerializer, 
                          ProductListSerializer, 
                          ReviewListSerializer, 
                          CategoryDetailSerializer,
                          ProductDetailSerializer,
                          ReviewDetailSerializer,
                          ProductReviewsSerializer)

@shop_api(['GET'])
def category_list_api_view(request):
    categories=Category.objects.all()
    data= CategoryListSerializer(categories, many=True).data 
    
    return Response(
        data=data,
    )

@shop_api(['GET'])
def product_list_api_view(request):
    products=Product.objects.all()
    data= ProductListSerializer(products, many=True).data 
    
    return Response(
        data=data,
    )
@shop_api(['GET'])
def review_list_api_view(request):
    reviews=Review.objects.all()
    data= ReviewListSerializer(reviews, many=True).data 
    return Response(
        data=data,
    )
@shop_api(['GET'])
def review_list_product_api_view(request):
    rating=Product.objects.all()
    data=ProductReviewsSerializer(rating, many=True).data
    return Response(
        data=data,
    )
@shop_api(['GET'])
def category_detail_api_view(request, id):
    try:
        categories=Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'this category is not found!'})
    data=CategoryDetailSerializer(categories, many=False).data
    
    return Response(data=data )

@shop_api(['GET'])
def product_detail_api_view(request, id):
    try:
        products=Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'this product is not found!'})
    data=ProductDetailSerializer(products, many=False).data
    
    return Response(data=data )

@shop_api(['GET'])
def review_detail_api_view(request, id):
    try:
        reviews=Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'this review is not found!'})
    data=ReviewDetailSerializer(reviews, many=False).data
    
    return Response(data=data )
