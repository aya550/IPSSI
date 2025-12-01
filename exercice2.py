print("entrez le premier nbr")
nbr1 = int(input())
print("entrez le deuxieme nbr")
nbr2 = int(input())    
print ("entrez le troisieme nbr")
nbr3 = int(input())

gr = max (nbr1, nbr2, nbr3)
pt = min (nbr1, nbr2, nbr3)

if (nbr1 != gr and nbr1 != pt) :
    print ("le nombre du milieu est :", nbr1)
elif (nbr2 != gr and nbr2 != pt) :
    print ("le nombre du milieu est :", nbr2)
elif (nbr3 != gr and nbr3 != pt) :
    print ("le nombre du milieu est :", nbr3)
