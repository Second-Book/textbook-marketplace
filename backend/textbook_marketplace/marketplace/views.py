from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Textbook, User
from .serializers import TextbookSerializer, SignupSerializer, CustomTokenObtainPairSerializer


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated
    

class TextbookListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
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
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PersonalCabinetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        pass

    def post(self, request):
        
        pass


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def get_queryset(self):
        return User.objects.all()