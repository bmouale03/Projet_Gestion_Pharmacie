from django.db import models

#class pour les categories des produits
class Categories(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
            return self.name

#Classe pour les produits
class Produits(models.Model):
    name=models.CharField(max_length=100)
    Category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantite=models.PositiveIntegerField(default=0) #PositiveIntegerField permet de prendre des valeures positives
    description=models.TextField()  #models.TextField permet de saisir de long texte
    date_ajout=models.DateTimeField(auto_now_add=True)  #dateTimefield permet de prendre la date et lheure
    date_expiration=models.DateField()    #datefield permet de prendre la date
    image=models.ImageField(null=True, blank=True, upload_to='media/')
    #action=models.CharField(max_length=100)
    class Meta:
        ordering =['-date_ajout']
    
    def statut_quantite(self):
       #si la quantite est egale a zero affiche rouge
       if self.quantite==0:
           return 'red'
       #sinon si la quantite est inferieur ou egal a 10 affiche orange
       elif self.quantite <=10:
           return 'orange'
       else:
           return 'green'
       
    def __str__(self):
            return self.name
        
#class pour les utilisateurs (client)
class Customer(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
            return self.name
    

class Vente(models.Model):
    produit=models.ForeignKey(Produits, on_delete=models.CASCADE)
    sale_date=models.DateTimeField(auto_now_add=True)
    quantite=models.PositiveBigIntegerField()
    customer=models.CharField(max_length=100)
    total_amount=models.DecimalField(max_digits=10 , decimal_places=2) #max_digits=10 , decimal_places=2 permet dafficher les nombres a virgule
    
    def __str__(self):
        return self.produit
    
class Facture_Client(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantite=models.PositiveBigIntegerField()
    date_chat=models.DateTimeField(auto_now_add=False)
    total_mount=models.ForeignKey(Vente, on_delete=models.CASCADE)
    produit=models.ForeignKey(Produits, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Le reçu de {self.Customer.customer}"
 
    
