from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Category, Product
from ..serializers import CategorySerializer, ProductSerializer

# category controller --------------------------------------------------------------------------------
@api_view(['GET'])
def getListCategory(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getCategoryById(request, id):
    category = Category.objects.get(category_id=id)
    serializer = CategorySerializer(category, many=False)

    return Response(serializer.data)

# get product by category id
@api_view(['GET'])
def getProductByCategoryId(request, id):
    products = Product.objects.filter(category_id=id)
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)