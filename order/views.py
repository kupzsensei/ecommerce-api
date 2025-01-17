from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OrderStatus
from .serializers import OrderStatusSerializer

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
