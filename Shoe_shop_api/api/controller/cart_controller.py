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