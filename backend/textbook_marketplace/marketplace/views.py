from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import SignupSerializer

from .models import Textbook, User
from .serializers import TextbookSerializer

class TextbookListView(APIView):
    permission_classes = []  # Allow unauthenticated requests
    def get(self, request):
        textbooks = Textbook.objects.all()
        serializer = TextbookSerializer(textbooks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TextbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TextbookDetailView(APIView):
    def get_object(self, pk):
        try:
            return Textbook.objects.get(pk=pk)
        except Textbook.DoesNotExist:
            return None

    def get(self, request, pk):
        textbook = self.get_object(pk)
        if textbook is not None:
            serializer = TextbookSerializer(textbook)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
class TextbookImageView(APIView): 
    def get(self, request, pk): 
        textbook = Textbook.objects.get(pk=pk) 
        image = textbook.image 
        return Response({'image': image.url})
    

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You have access to this protected view!"})
    

class SignupView(APIView):
    permission_classes = []  # Allow unauthenticated requests
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    