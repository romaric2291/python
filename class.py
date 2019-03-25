class Voiture:
    def __init__(self,nom,marque,annee):
        self.nom = nom
        self.marque = marque
        self.annee = annee

c = Voiture("Laguna","Renault",1956)

print(c.nom)