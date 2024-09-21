from django.forms import ModelForm
from .models import Produits , Categories
from django import forms

class AjoutProduit(ModelForm):
    class Meta:
        model = Produits
        fields=[
            'name','Category','price','quantite','description'
            ,'date_expiration', 'image'   
        ]
        widgets={
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Entrez le nom du produit',
                    'class': 'form-control' #cette class permet de styliser le formulaire Django
                }
            ),
            
            'Category': forms.Select(
                attrs={
                    'class': 'forms-control'
                }
            ),
            
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Entrez le prix du produit',
                    'class': 'form-control'
                }
            ),
            
            'quantite': forms.NumberInput(
                attrs={
                    'placeholder': 'Entrez la quantité',
                    'class': 'form-control'
                }
            ),
            
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Donnez une petite d\'escription du produit',
                    'class': 'form-control',
                    'rows': 4
                }
            ),
            
            'date_expiration': forms.DateInput(
                attrs={
                    'placeholder': 'Date d\'expiration',
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                }
            )
        }
        
        
        #Gestion des erreurs
    def __init__(self, *args, **kwargs):
        super(AjoutProduit, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages={
            'required': 'Le nom est obligatoire',
            'invalid': 'Veuillez renseigner le nom'
        }
        
        self.fields['Category'].error_messages = {
            'required':'La categorie est obligatoire',
            'invalid': 'Veuillez selectionner la categorie'
        }
        
        self.fields['price'].error_messages = {
            'required':'Le prix est obligatoire',
            'invalid': 'Veuillez entrer le prix'
        }
        
        self.fields['quantite'].error_messages = {
            'required':'La quantité est obligatoire',
            'invalid': 'Veuillez entrer la quantité'
        }
        
        self.fields['description'].error_messages = {
            'required':'La description est obligatoire',
            'invalid': 'Veuillez entrer la description'
        }
        self.fields['date_expiration'].error_messages = {
            'required':'La date d\'expiration' 'est obligatoire',
            'invalid': 'Veuillez entrer la date d\'expiration'
        }
            
            
        

    
