mois = input("Entrez le nom du mois : ")

if mois in ['Janvier', 'Mars', 'Mai', 'Juillet', 'Août', 'Octobre', 'Décembre']:
    jours = 31
elif mois in ['Avril', 'Juin', 'Septembre', 'Novembre']:
    jours = 30
elif mois == 'Février':
    jours = 28
else:
    jours = None
    print("error.")

print("Le mois de", mois,"a", jours,"jours.")
