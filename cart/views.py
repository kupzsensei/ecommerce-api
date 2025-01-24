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
        print(data,  'cart data')
        serializer = PostCartSerializer(data={"product": data['product'] , "quantity": data['quantity'] , "user": request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self , request):
        try:
            instance = Cart.objects.get(id=request.data['id'])
            serializer = PostCartSerializer(instance , data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"ok": True , 'data':serializer.data})
            return Response({'ok': False , 'error': serializer.errors})
        except Cart.DoesNotExist:
            return Response({"detail": 'Product does not exist.'})
    
    def delete(self , request):
        try:
            instance = Cart.objects.get(id=request.data['id'])
            instance.delete()
            return Response({'ok': True , 'detail': "deleted"})
        except Cart.DoesNotExist:
            return Response({"detail": 'Product does not exist.'})