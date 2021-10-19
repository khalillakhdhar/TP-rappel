myList = [1, 2, 20, -4, 5, 12, 7, -8, 3, 10]
somme=0
for i in myList:
    if(i<0):
        print(i)
    somme+=i
print("la somme des éléments du tableau est: "+str(somme))
