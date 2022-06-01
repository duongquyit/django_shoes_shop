from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Bill
from ..serializers import BillSerializer

# bill controller ------------------------------------------------------------------------------------
@api_view(['GET'])
def getListDetailBill(request):
    bills = Bill.objects.all()
    serializer = BillSerializer(bills, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getBillById(request, id):
    bill = Bill.objects.get(bill_id=id)
    serializer = BillSerializer(bill, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def createBill(request):
    serializer = BillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)