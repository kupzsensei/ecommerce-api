from django.shortcuts import render
from rest_framework.views import APIView
from .models import Cart
from .serializers import CartSerializer , PostCartSerializer
from rest_framework.response import Response
# Create your views here.
class CartView(APIView):

    def get(self , request):
        data = Cart.objects.all().filter(user=request.user.id).order_by('-id')
        print(request.user.id)
        serializer = CartSerializer(data , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        data = request.data
        serializer = PostCartSerializer(data={**data , "user": request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)