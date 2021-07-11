from rest_framework import serializers
from .models import Product, Category, Company, ProductSize, ProductSite, Comment, CustomerReportRecord
from django.contrib.auth.models import User
from django.utils.timezone import now
from versatileimagefield.serializers import VersatileImageFieldSerializer

from rest_flex_fields import FlexFieldsModelSerializer


from rest_flex_fields import FlexFieldsModelSerializer

class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
          'category': (CategorySerializer, {'many': True})
        }


class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
          'products': ('reviews.ProductSerializer', {'many': True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('reviews.CategorySerializer', {'many': True}),
            'sites': ('reviews.ProductSiteSerializer', {'many': True}),
            'comments': ('reviews.CommentSerializer', {'many': True}),
            'image': ('reviews.ImageSerializer', {'many': True}),
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'productsize': 'reviews.ProductSizeSerializer',
            'company': 'reviews.CompanySerializer',
        }





class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'user': 'reviews.UserSerializer'
        }


class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReportRecord

    
    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("error message")
        
        return value

    def validate(self, data):
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get('content', instance.title)
        instance.save()
        return instance


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



# class ImageSerializer(FlexFieldsModelSerializer):
#     image = VersatileImageFieldSerializer(
#         sizes='product_headshot'
#     )

#     class Meta:
#         model = Image
#         fields = ['pk', 'name', 'image']


