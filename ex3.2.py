x = int(input('Veuillez entrer un entier : '))
y = int(input('Veuillez entrer un deuxième entier : '))
if x == 0 or y == 0:
    print('Le produit de \"', x, '\" et \"', y, '\" est : NUL')
else:
    if x > 0:
        if y > 0:
            print('Le produit de \"', x, '\" et \"', y, '\" est : POSITIF')
        else:
            print('Le produit de \"', x, '\" et \"', y, '\" est : NÉGATIF')
    else:
        if y > 0:
            print('Le produit de \"', x, '\" et \"', y, '\" est : NÉGATIF')
        else:
            print('Le produit de \"', x, '\" et \"', y, '\" est : POSITIF')
