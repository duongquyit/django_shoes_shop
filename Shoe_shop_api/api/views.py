from functools import reduce
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import AmountSerializer, CategorySerializer, ProductSerializer, SizeSerializer, BillSerializer, UserSerializer

from .models import Category, Product, Size, Amount, Detail_Bill, User

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

            

# Size controller ------------------------------------------------------------------------------------
@api_view(['GET'])
def getListSize(request):
    sizes = Size.objects.all()
    serializer = SizeSerializer(sizes, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getSizeDetail(request, id):
    size = Size.objects.get(size_id=id)
    serializer = SizeSerializer(size, many=False)

    return Response(serializer.data)

# Amount controller ------------------------------------------------------------------------------------
@api_view(['GET'])
def getListAmounts(request):
    amounts = Amount.objects.all()
    serializer = AmountSerializer(amounts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getAmountDetail(request, id):
    amount = Amount.objects.get(amount_id = id)
    serializer = AmountSerializer(amount, many=False)

    return Response(serializer.data)

# detail_bill controller ------------------------------------------------------------------------------------
@api_view(['GET'])
def getListDetailBill(request):
    bills = Detail_Bill.objects.all()
    serializer = BillSerializer(bills, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getDetailBill(request, id):
    bill = Detail_Bill.objects.get(bill_id=id)
    serializer = BillSerializer(bill, many=False)

    return Response(serializer.data)

# user controller --------------------------------------------------------------------------------
@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

