from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import AjoutProduit
from django.contrib import messages
from datetime import datetime, timedelta, tzinfo
from .models import *


class Affichage (ListView):
    #Affichage du template
    template_name = 'home.html'
    #Recuperation de donnees
    queryset= Produits.objects.all()
    
#Class Django d4qjout des donnees

class AjoutProduits(CreateView):
    # Utilisation du model
    model = Produits
    # specifier le formulaire
    form_class = AjoutProduit
    # Affichage du template
    template_name = 'ajout_donnees.html'
    #redirection apres enrregistrement
    success_url = reverse_lazy('home')
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
#def home(request):
    #Recuperer toutes les donnees dans la BD
    ##context={
       # 'donnees': donnees
   # }
    
   # return render(request,'home.html', context)
   
# Fonction ajout des donnees
#def ajout_donnees(request):
    #Creation de la variable de gestion des erreurs
    #name = request.POST['name']
        ###date_expiration = request.POST['date_expiration']
        ##ry:
           ##except ValueError:
            #errors['date_expiration']= "Le format n'est pas correct. Essayez cece: AAAA-MM-JJ"
        #Validation du prix
        #try:
            #price = float(price)
            #if price < 0 :
                #errors['price_str'] = "Le prix ne peut pas etre negatif"
        #except ValueError:
            #errors['price'] = "Entrez le prix valide SVP"
        # Si il n'y aucune erreur
        #if not errors:
            #try:
                #Recuperation des categories dans la table en fonction de la cle primaire
                #Category=Categories.objects.get(pk=request.POST['Category'])
                #savedonnees=Produits(name= name, price=price, quantite=quantite,
                                    #description=description,date_expiration=date_expiration,
                                    #image=image, Category=Category)
                #savedonnees.save()
                #messages.success( request, "Le produit a été ajouté avec succès")
            #except Categories.DoesNotExist:
                #errors ['category']=f'La categorie indiquée est introuvable.'
            #except KeyError as e:
                #errors[str(e)]= f'Le champ {e} est manquant dans la requete.'
            #except Exception as e:
               # messages.error(request , f'Une erreur est survenue:{e}')
        
        #return redirect('home')
    #else:
         #Category=Categories.objects.all
    #return render(request, "ajout_donnees.html", {"Category": Category, "errors": errors})





