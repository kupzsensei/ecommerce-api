from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

class UserView(APIView):
    permission_classes = [AllowAny]
    def get(self , request):
        data = User.objects.all().order_by('-id')
        serializer = UserSerializer(data , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
           
            return Response({'detail': "Account Created."})
        return Response({'ok': False ,  'error': serializer.errors})
    

    def patch(self , request):
        try:
            instance = User.objects.get(id=request.data['id'])
            serializer = UserSerializer(instance , data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"ok": True , "detail": "account update success."})
            return Response ({"ok":False , "error": serializer.errors})
        except User.DoesNotExist:
            return Response({"ok": False , "detail" : "User Does not exist."})