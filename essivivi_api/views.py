from urllib import request
from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib import auth
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import uuid
import jwt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

# Create your views here.
class LoginView(generics.GenericAPIView, ObtainAuthToken):
    serializer_class =  UserLoginSerializer
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                    status=status.HTTP_400_BAD_REQUEST)
        user = auth.authenticate(username = username, password = password)

        if user:
            # if user.is_agent == False:
            
            #     return Response({
            #         'status':'acces lock',
            #         'error': 'Cette page n\'est pas destiné à vous'
            #         },
            #         status=status.HTTP_400_BAD_REQUEST)

            token, created = Token.objects.get_or_create(user = user)
            serializer = UserSerializer(user)
    

            data = {
                'user': serializer.data,
                'message': 'success',
                'status': 'Ok',
                'token': token.key
            }
            return Response(data, status= status.HTTP_200_OK)

        #Response
        return Response({
            'status':'invalid',
            'detail': 'Invalid credentials'
            }, 
            status= status.HTTP_401_UNAUTHORIZED)

# Registration API View
class RegisterView(generics.GenericAPIView):
    
    serializer_class =  RegisterSerializer
    
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "RequestId": str(uuid.uuid4()),
                    "Message": "User created successfully",
                    "User": serializer.data,
                }, status = status.HTTP_201_CREATED
                )
        return Response({"Error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


class RegisterAgentView(generics.GenericAPIView):
    
    serializer_class =  RegisterAgentSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "RequestId": str(uuid.uuid4()),
                    "Message": "User created successfully",
                    "User": serializer.data,
                }, status = status.HTTP_201_CREATED
                )
        return Response({"Error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

# Function pour faire la mise à jour d'un produit

def Update_stock(nbr_eaux, stock_livre, stock_restant, stock_modif):
    if stock_modif > stock_livre:
        stock_restant = nbr_eaux + stock_livre - stock_modif
        return stock_restant
    elif stock_modif < stock_livre:
        stock_restant = nbr_eaux + stock_livre - stock_modif
        return stock_restant
    else:
        return stock_restant

# View For Categories
class ListCategories(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Categories.objects.all()
    serializer_class = CategorieSerializer

class DetailCategories(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Categories.objects.all()
    serializer_class = CategorieSerializer

# View For Eau
class ListEau(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Eau.objects.all()
    serializer_class = EauSerializer

class DetailEau(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Eau.objects.all()
    serializer_class = EauSerializer


# View For User
class ListUser(generics.ListCreateAPIView):
    #  permission_classes = (permissions.IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View For Agent
class ListAgent(generics.CreateAPIView):
    # # permission_classes = (permissions.IsAuthenticated)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class DetailAgent(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


"""
Crud concernant les activiés 

"""
class AgentList(APIView):

    """
    List all Agents, or create a new Agent.
    """
     
    def get(self, request):
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many = True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AgentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            agent = User.objects.filter(gerant = pk)
            return agent
            #return Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        agent = self.get_object(pk)
        serializer = UserSerializer(agent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        agent = self.get_object(pk)
        serializer = AgentSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        agent = self.get_object(pk)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



# View For Client
class ListClient(generics.CreateAPIView):
    # # permission_classes = (permissions.IsAuthenticated)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DetailClient(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Livraison View
class ListLivraison(generics.CreateAPIView):
    # # permission_classes = (permissions.IsAuthenticated)
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer

class DetailLivraison(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer

