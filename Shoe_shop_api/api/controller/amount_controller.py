from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Amount
from ..serializers import AmountSerializer

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

@api_view(['GET'])
def getAmountByProductIdAndSizeId(request, product_id, size_id):
    amount = Amount.objects.filter(product = product_id, size = size_id)
    amountProductWithSize = 0;
    serializer = AmountSerializer(amount, many=True)
    for value in serializer.data:
        amountProductWithSize += value['quantity']
    
    return Response(amountProductWithSize)