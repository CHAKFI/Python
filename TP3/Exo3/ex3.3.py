nbr = int(input('Veuillez entrer entrer : \n'))

if nbr < 10:
    print('Prix : 5 DH')
elif nbr >= 10:
    if nbr <= 20:
        print('Prix : 4 DH')
elif nbr >= 20:
        print('Prix : 3 DH')