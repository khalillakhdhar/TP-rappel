x=int(input("donner un entier"))
i=2
while x%i!=0 and i<x:
    i=i+1
if(i<x):
    print("n'est pas premier")
else:
    print("premier")