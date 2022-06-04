from numpy import product
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Cart
from ..serializers import CartSerializer
# cart controller ------------------------------------------------------------------------------------
@api_view(['GET'])
def getCartByUserId(request, user_id):
    carts = Cart.objects.filter(user_id = user_id)
    serializer = CartSerializer(carts, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def updateProductQuantity(request, id):
    Cart.objects.filter(cart_id=id).update(quantity=request.data["quantity"])
    return Response({"title": 'update quantity product successfully!'})

@api_view(['POST'])
def createCart(request):
    cart = Cart.objects.create(user_id=request.data["user"],product_id=request.data["product"],size_id=request.data["size"],quantity=request.data["quantity"])
    serializer = CartSerializer(instance=cart)
    
    return Response(serializer.data)

@api_view(['POST'])
def deleteCartById(request, id):
    Cart.objects.get(cart_id=id).delete()

    return Response({"title": 'Delete successfully!'})