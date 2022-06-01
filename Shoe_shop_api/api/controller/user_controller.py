from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import UserSerializer
from ..models import User
# user controller --------------------------------------------------------------------------------
@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getUserById(request, id):
    try:
        user = User.objects.get(user_id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response({"title":'User can not found'})

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)
    # OR
    # try:
    #     user = User.objects.get(username=request.data["username"])
    #     if user:
    #         return Response({"title":'Username is exist!'})
    # except:
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)

@api_view(['POST'])
def signIn(request):
    try:
        user = User.objects.get(username=request.data["username"])
        serializer = UserSerializer(instance=user, many=False)
        if(serializer.data["password"] != request.data["password"]):
            return Response({"title":"Password is incorrect!"})
        return Response(serializer.data)
    except:
        return Response({"title": 'Username not exist!'})
