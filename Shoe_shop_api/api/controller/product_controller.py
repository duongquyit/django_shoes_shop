from api.serializers import AmountSerializer, CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Amount, Category, Product
# product controller ------------------------------------------------------------------------------------

@api_view(['GET'])
def getListProduct(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProductDetail(request, id):
    product = Product.objects.get(product_id=id)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def getOutstandingProducts(request):
    categories = Category.objects.all()
    categorySerializer = CategorySerializer(categories, many=True)
    outstandingProducts = []
    for category in categorySerializer.data:
        product = Product.objects.filter(category_id=list(category.values())[0])[:3]
        for item in product:
            outstandingProducts.append(item)
    
    productSerializer = ProductSerializer(outstandingProducts, many=True)

    return Response(productSerializer.data)


@api_view(['GET'])
def getAmountProduct(request, id):
    amount = Amount.objects.filter(product_id=id)
    serializer = AmountSerializer(amount, many=True)

    return Response(serializer.data)
            