x=int(input("donner un entier 1 "))
y=int(input("donner un entier 2"))
a=x
b=y
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
ppc=(x*y)/a
print("le ppcm de %s et %s est %s"%(x,y,ppc)) #%s