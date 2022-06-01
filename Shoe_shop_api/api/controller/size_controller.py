
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Size
from ..serializers import SizeSerializer
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