n = int(input("Veuillez saisir un nombre \n"))
S=0
for i in range(0,n):
    if(i%2 == 0):
        S=S+i
print("La somme est : ",S)