chaine = input("Entrez une chaîne de caractères : ")
longueur = len(chaine)
lettres=[]
chiffres=[]
for i in range (longueur):
    if chaine[i].isalpha():
        lettres.append(chaine[i])
    
    elif chaine[i].isdigit():
        chiffres.append(chaine[i])
print("Lettres :", len(lettres))
print("Chiffres :", len(chiffres))
