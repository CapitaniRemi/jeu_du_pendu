alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pas_valide=True
while pas_valide:
	print("--------------\n JEU DU PENDU\n--------------\n")
	mot=input("Joueur 1, entrez le mot mystère : ").upper()
	pas_valide=False
	for car in mot:
		if car not in alphabet:pas_valide=True
	if pas_valide:
		print("MOT NON VALIDE")
		input("Pressez Entrer pour recommencer")


ca_joue=True
gagne=False
perdu=False
jokers=6
chaine="-"*len(mot)
proposees=""

while ca_joue:
    print("--------------\n JEU DU PENDU\n--------------\n")
    print("Mot inconnu : ",chaine)
    print("Lettres déjà proposées : ",proposees)
    print("Jokers : ",jokers)
    lettre=input("Joueur 2, proposez une lettre : ").upper()
    if lettre in alphabet and len(lettre)==1 :
        if lettre not in proposees:
            proposees=proposees+lettre
            if lettre in mot:


                nouvelle_chaine=''
                for i in range(len(mot)):
                                        if mot[i]==lettre : nouvelle_chaine=nouvelle_chaine+lettre
                                        else : nouvelle_chaine=nouvelle_chaine+chaine[i]
                chaine=nouvelle_chaine
            else:
                jokers=jokers-1

            proposees+=lettre
        else : print('Lettre déjà proposée')
    else: print("CE N'EST PAS UNE LETTRE!")
    if chaine==mot:
        gagne=True
        print("Bien joué, tu as gagné !")
    if jokers==0:
        perdu=True
        print("Dommage, une prochaine fois")

    ca_joue= not(gagne or perdu)

if gagne:
	print("\nVOUS AVEZ GAGNE")
	if jokers==0:print("C'ETAIT JUSTE!")
	elif jokers==6:print("0 FAUTE : Tékro faure!")
else: print("\nVous avez perdu c'est trop dommage woula")
print("Le mot était ",mot)
