from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField( max_length= 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Catégoires'

    def __str__(self):
        return self.title

class Eau(models.Model):
    title = models.CharField(max_length=100, null= True)
    user = models.ForeignKey(
        User, 
        on_delete= models.CASCADE, 
        related_name='eaux',
        blank=True, 
        null= True
        )
    categorie = models.ForeignKey(
        Categories, 
        on_delete= models.CASCADE, 
        related_name='eaux',
        blank=True, 
        null= True)
    description = models.TextField()
    prix = models.IntegerField()
    qteStock = models.IntegerField(null= True)
    # status = models.BooleanField(default= True)
    image = models.ImageField(upload_to= 'images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True) 

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Eaux'

    def __str__(self):
        return self.title


class Agent(models.Model):
    user = models.ForeignKey(User, related_name='eauxRecue', on_delete= models.SET_NULL, blank=True,  null= True)
    produit = models.ForeignKey(Eau, on_delete= models.CASCADE, blank=True,  null= True)
    nom_agent = models.CharField(max_length= 255, null= True)
    nom_produit = models.CharField(max_length= 255, null= True)
    nbr_eaux = models.IntegerField()
    gerant_id = models.IntegerField(null= True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user', '-created_at']

    def __str__(self):
        return f'{self.user}'
    

class Client(models.Model):
    user = models.ForeignKey(User, related_name='clients', on_delete= models.SET_NULL, blank=True, null= True)
    nom = models.CharField(max_length= 255)
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length= 10)

class Livraison(models.Model):
    agent = models.ForeignKey(User, on_delete= models.SET_NULL, blank=True, null= True)
    produit = models.ForeignKey(Eau, on_delete= models.SET_NULL, blank=True, null= True)
    client = models.ForeignKey(Client, on_delete= models.SET_NULL, blank=True, null= True)
    stock_livrer = models.IntegerField()
    Date_livraison = models.DateTimeField(auto_now_add= True)
 