try:
    j=int(input("donnez le jour"))
    m=int(input("donnez le mois"))
    a=int(input("donnez l anné"))
except:
    print("la date doit être numérique")
if j<1 or m<1 or a<1:
    print("les paramétres doivent être positif")
elif j>31 or m>12 or a<1900:
    print("limite dépassé")
else:
    if m==4 or m==6 or m==9 or m==11:
        if j<=30:
            print("date correcte")
        else:
            print("date incorrecte")
    elif m==2:
        if a%4==0:
            if j<=29:
                print("date correcte")
            else:
                print("date incorrecte")
        else:
            if j<=28:
                print("date correcte")
            else:
                print("date incorrecte")
    else:
        if j<=31:
            print("date correcte")
        else:
            print("date incorrecte")

