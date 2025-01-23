from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OrderStatus , ShippingAddress , Order
from .serializers import OrderStatusSerializer , ShippingAddressGetSerializer , ShippingAddressSerializer  , OrderSerializerGet , OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly 

# Create your views here.
class OrderStatusView(APIView):

    def get(self, request): # for read
        data = OrderStatus.objects.all().filter(deleted=False)
        serializer = OrderStatusSerializer(data , many=True)
        return Response(serializer.data)
    
    def post(self, request): # for create / add
        data = request.data
        serializer = OrderStatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "data":serializer.data })
        return Response({"ok": False , 'errors': serializer.errors})
        

    def patch(self,request): # for update / edit
        data = request.data
        try:
            row_instance = OrderStatus.objects.get(id=data['id'])
            serializer = OrderStatusSerializer(row_instance , data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"ok" : True , "data": serializer.data})
            return Response({"ok": False , "errors": serializer.errors})

        except OrderStatus.DoesNotExist:
            return Response({"ok": False , "error" : "Walang ganyang data sa aming database!"})

    def delete(self,request): # for delete
        data = request.data
        try:
            row_instance = OrderStatus.objects.get(id=data['id'])
            serializer = OrderStatusSerializer(row_instance , data={"deleted": True} , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"ok": True , "msg": "Deleted na ang iyong data , mag bunyi" })
            return Response({"ok":False , "msg": "invalid transaction"})

        except OrderStatus.DoesNotExist:
            return Response({"ok": False , "error" : "Walang ganyang data sa aming database!"})



class ShippingAddressView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request): # for read
        data = ShippingAddress.objects.all().order_by('-id')
        serializer = ShippingAddressGetSerializer(data , many=True)
        return Response(serializer.data)
    
    def post(self, request): # for create / add
        # data = request.data
        serializer = ShippingAddressSerializer(data={**request.data , 'user':request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "data":serializer.data })
        return Response({"ok": False , 'errors': serializer.errors})
        

    def patch(self,request): # for update / edit
        data = request.data
        try:
            row_instance = ShippingAddress.objects.get(id=data['id'])
            serializer = ShippingAddressSerializer(row_instance , data=data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"ok" : True , "data": serializer.data})
            return Response({"ok": False , "errors": serializer.errors})

        except OrderStatus.DoesNotExist:
            return Response({"ok": False , "error" : "Walang ganyang data sa aming database!"})

    def delete(self,request): # for delete
        data = request.data
        try:
            row_instance = ShippingAddress.objects.get(id=data['id'])
            row_instance.delete()
            return Response({"ok": True , "msg": "Deleted na ang iyong data , mag bunyi" })

        except OrderStatus.DoesNotExist:
            return Response({"ok": False , "error" : "Walang ganyang data sa aming database!"})

class OrderView(APIView):
    
    def get(self, request):
        data = Order.objects.all().order_by('-id')
        serializer = OrderSerializerGet(data , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        data = request.data
        
        serializer = OrderSerializer(data={**data, 'user': request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data})
        return Response({'ok': False , 'error': serializer.errors})
    

    def patch(self, request):
        data = request.data
        try:
            instance = Order.objects.get(id=data['id'])
            serializer = OrderSerializer(instance , data=data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'ok': True , 'msg': 'update success'})
            return Response({'ok': False , 'error': serializer.errors})
        except Order.DoesNotExist:
            return Response({'msg': "order does not exist."})