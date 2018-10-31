PrixHT = float(input('Le prixHT ? \n'))
nbr_artc = int(input('Combien d_articles avez-vous pris ? \n'))
print('TVA = 20%')
TVA = 0.2
TTC = PrixHT+(PrixHT*TVA)
P_tot = nbr_artc*TTC
print('********* Le prix TOTAL est : ',P_tot,' MAD *********')