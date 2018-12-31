x = int(input("Veuillez entrer x: "))
y = int(input("Veuillez entrer y: "))
while(x>y):
    x = int(input("Veuillez entrer x: "))
    y = int(input("Veuillez entrer y: "))
for i in range(x,y):
    if(i%2 == 0):
        print("les chiffres pairs entre ",x," et ",y," sont: ",i)




