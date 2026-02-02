
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

@shop_api(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories=Category.objects.all()
        data= CategoryListSerializer(categories, many=True).data 
        return Response(
            data=data,
    )
    elif request.method == 'POST':
        name=request.data.get('name')
        categories=Category.objects.create(name=name)
        
    return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(categories).data)
        

@shop_api(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products=Product.objects.all()
        data= ProductListSerializer(products, many=True).data 
        return Response(
          data=data,
          )
    elif request.method == 'POST':
        title=request.data.get('title')
        description=request.data.get('description')
        price= request.data.get('price')
        category_id=request.data.get('category_id')
        products=Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(products).data)
          
@shop_api(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews=Review.objects.all()
        data= ReviewListSerializer(reviews, many=True).data 
        return Response(
        data=data,
         )
    elif request.method == 'POST':
        text=request.data.get('text')
        product_id=request.data.get('product_id')
        stars=request.data.get('stars')
        reviews=Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(reviews).data)
@shop_api(['GET'])
def review_list_product_api_view(request):
    rating=Product.objects.all()
    data=ProductReviewsSerializer(rating, many=True).data
    return Response(
        data=data,
    )
@shop_api(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        categories=Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'this category is not found!'})
    if request.method == 'GET':
        data=CategoryDetailSerializer(categories, many=False).data
        return Response(data=data )
    elif request.method == 'PUT':
        categories.name=request.data.get('name')
        categories.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=CategoryDetailSerializer(categories).data)
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@shop_api(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        products=Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'this product is not found!'})
    if request.method == 'GET':
       data=ProductDetailSerializer(products, many=False).data
       return Response(data=data )
    elif request.method == 'PUT':
        products.title=request.data.get('title')
        products.description=request.data.get('description')
        products.price=request.data.get('price')
        products.category_id=request.data.get('category_id')
        products.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(products).data)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@shop_api(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        reviews=Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'this review is not found!'})
    if request.method == 'GET':
         data=ReviewDetailSerializer(reviews, many=False).data
         return Response(data=data )
    elif request.method == 'PUT':
        reviews.text=request.data.get('text')
        reviews.product_id=request.data.get('product_id')
        reviews.stars=request.data.get('stars')
        reviews.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(reviews).data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
