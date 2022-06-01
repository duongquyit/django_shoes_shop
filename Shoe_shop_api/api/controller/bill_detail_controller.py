from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Bill_Detail
from ..serializers import BillDetailsSerializer
# bill detail controller --------------------------------------------------------------------------------
@api_view(['GET'])
def getAllBillDetails(request):
    bills = Bill_Detail.objects.all()
    serializer = BillDetailsSerializer(bills, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getBillDetailById(request, id):
    bill = Bill_Detail.objects.get(bill_detais_id=id)
    serializer = BillDetailsSerializer(bill, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def createBillDetail(request):
    serializer = BillDetailsSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)