from .models import User
from .serializers import UserSerialiser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
#from rest_framework import viewsets

@api_view(['GET', 'POST'])
def User_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerialiser(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def User_detail(request,pk):
    try:
        user=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    if request.method=='GET':
        serilizer=UserSerialiser(user)
        return Response(serilizer.data)
    elif request.method=='PUT':
        serializer = UserSerialiser(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=="DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       







def gg_form(request):
    return render(request,"base.html")








"""class UserViewSet(viewsets.ReadOnlyModelViewSet):
    
    #This viewset automatically provides `list` and `detail` actions.
    
    queryset =User.objects.all()
    serializer_class = UserSerialiser"""
#curl -i -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/user/users/ -d '{"Cin": "15009060",
        #"Name": "Iline",
        #"Email": "lina@outlook.com"}'    