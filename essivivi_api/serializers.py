from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 50, min_length = 6)
    email = serializers.CharField(max_length = 50, min_length = 6)
    password = serializers.CharField(max_length = 255, min_length = 6, write_only=True)
    #is_manager = serializers.BooleanField(default=True, read_only= True)

    class Meta:
        model = User
        fields = ["last_name", "first_name", "username", "email", "password"]
    
    def validate(self, args):
        email= args.get('email', '')
        username = args.get('username', '')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('Email is already exists')})
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({'username': ('username is already exists')})
        return super().validate(args)


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RegisterAgentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 50, min_length = 6)
    email = serializers.CharField(max_length = 50, min_length = 6)
    password = serializers.CharField(max_length = 255, min_length = 6, write_only=True)
    is_agent = serializers.BooleanField()

    class Meta:
        model = User
        fields = ["id", "last_name", "first_name", "username", "email", "password", "is_agent", "gerant"]
    
    def validate(self, args):
        email= args.get('email', '')
        username = args.get('username', '')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('Email is already exists')})
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({'username': ('username is already exists')})
        return super().validate(args)


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# User login Serializer
class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 65, 
        min_length = 6, 
        write_only=True
    )


    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, attrs):
        email= attrs.get('email', '')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('Email is already in user')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


"""
    Model Serializer
"""

class CategorieSerializer(serializers.ModelSerializer):
    #produits = serializers.StringRelatedField(many=True)
    class Meta:
        model = Categories
        fields = {"id", "title", "description", "produits"}
        fields = '__all__'


class EauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eau
        fields = {"id", "categorie", "title", "description", "prix", "qteStock", "imagUrl", "created_at"}
        fields = '__all__'

#General Agent User Serializer
class UserAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username",  "last_name", "first_name", "email", "is_agent"]

class UserAgent(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name"]


class EauAgent(serializers.ModelSerializer):
    class Meta:
        model = Eau
        fields = ["title"]


# Agent Serializer
class AgentSerializer(serializers.ModelSerializer):
    #user = UserAgent()
    #produit = EauAgent()
    class Meta:
        model = Agent
        fields = ["id", "user", "gerant_id", "produit", "nbr_eaux", "created_at"]

    def create(self, validated_data):
        produit_data = validated_data.get('produit')
        prod = Eau.objects.get(title = produit_data.title)
        
        if validated_data.get('nbr_eaux') > 0:
            agent = Agent.objects.create(**validated_data)
            if prod.qteStock == 0:
                raise serializers.ValidationError({'stock': ('Votre stock est vide ')})
            elif prod.qteStock < validated_data.get('nbr_eaux'):
                raise serializers.ValidationError({'nbr_eau': ('Le nombre que vous entrez est supérieur au stock ')})
            elif prod.qteStock == validated_data.get('nbr_eaux'):
                raise serializers.ValidationError({'nbr_eau': ('Le nombre que vous entrez est égal au qte_Stock ')})
            prod.qteStock = prod.qteStock - validated_data.get('nbr_eaux')

        else:
            raise serializers.ValidationError({'nbr_eau': ('Le nombre entré doit être positif ')})

        prod.save()

        return agent

    def update(self, instance, validated_data):
        produit_data = validated_data.get('produit')
        prod = Eau.objects.get(id = produit_data.id)
        #produit = instance.produit
        instance.nbr_eaux = validated_data.get('nbr_eaux', instance.nbr_eaux)
        instance.save()
        prod.stock = prod.stock + instance.nbr_eaux - validated_data.pop('nbr_eaux')

        prod.save()
        
        return instance

# Client Serializers
class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ["user", "nom", "email", "adresse", "telephone"]

    def validate(self, args):
        email= args.get('email', '')
        nom = args.get('nom', '')
        if Client.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('Email is already exists')})
        if Client.objects.filter(nom = nom).exists():
            raise serializers.ValidationError({'nom': ('nom is already exists')})
        return super().validate(args)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

# User General serializer
class UserSerializer(serializers.ModelSerializer):
    agents = UserAgentSerializer(many = True)
    eaux = EauSerializer(many = True)
    eauxRecue = AgentSerializer(many = True)
    clients = ClientSerializer(many = True)
    class Meta:
        model = User
        fields = ["id", "last_name", "first_name", "email", "is_agent",  "is_manager", "agents", "gerant", "clients", "eaux", "eauxRecue"]


# class UserAgentSerializer(serializers.ModelSerializer):
#     #agents = UserAgentSerializer(many = True)
#     eaux = EauSerializer(many = True)
#     class Meta:
#         model = User
#         fields = ["id", "username", "agents"]

class UserAgEauSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eau
        fields = ["id", "title"]

class UserGerantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "first_name"]





#Livraison Seriralizers
class LivraisonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livraison
        fields = ["agent","produit", "client", "stock_livrer", "Date_livraison"]

    def create(self, validated_data):
        user_data = validated_data.get('agent')
        produit_data = validated_data.get('produit')

        agent = Agent.objects.get(user = user_data.id, produit = produit_data)
        
        if validated_data.get('stock_livrer') > 0:
            livraison = Livraison.objects.create(**validated_data)
            if agent.nbr_eaux == 0:
                raise serializers.ValidationError({'stock': ('Votre stock est vide ')})
            elif agent.nbr_eaux < validated_data.get('stock_livrer'):
                raise serializers.ValidationError({'nbr_eau': ('Le nombre que vous entrez est supérieur au stock ')})
            elif agent.nbr_eaux == validated_data.get('stock_livrer'):
                raise serializers.ValidationError({'nbr_eau': ('Le nombre que vous entrez est égal au qte_Stock ')})
            agent.nbr_eaux = agent.nbr_eaux - validated_data.get('stock_livrer')

        else:
            raise serializers.ValidationError({'nbr_eau': ('Le nombre entré doit être positif ')})

        agent.save()

        return livraison