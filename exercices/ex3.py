valeur= 7000100
compteur=0
augmentation=valeur
temp=valeur
for x in range(101):
    temp=temp*1.01
print("la valeur d'augment durant 101 ans sera %s"%(temp))
while augmentation<(valeur*2):
    compteur=compteur+1
    augmentation=augmentation*1.01
print("le nombre des années nécessaire pour doubler le prix est:%s "%(compteur))