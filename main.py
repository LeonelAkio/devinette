#créé par Leonel Akio Briones et Xavier Willoughby
#Jeu de devinette de nombre

#from numpy import *
#from var.txt import score
import random
#from pickle import *
nombreEssais = 0               
essai = -1
score=0
inconnu = random.randint(0, 1000)    

print(inconnu)
highscore=0
#Test du système de sauvegardement qui ne vas probablement pas marcher

#dump(highscore, open("data.txt","wb"))
#d=open("data.txt","r")

#print(d.read())

while (essai != inconnu) :
	essai = int(input("Entrez un chiffre de 0 à 1000 :"))
	vérifie=input("Voulez vous vérifier l'essai (oui|non)\n")
	nombreEssais += 1
	if vérifie==("oui"):
		if essai != inconnu :
#le text qui apparait quand la réponse est mauvaise
			print("Mauvaise réponse, vous avez essayé : %d fois sans réussir \n"%nombreEssais)
			if essai>=inconnu:
				print("le nombre est plus plus petit")
			else:
				print("le nombre est plus grand")
		else :

#le text qui apparait quand la réponse est bonne
			
			score += 1
			print("\n\nBravo! Votre score est : %d"%score)
			choice=input("\n Voulez vous recomencer: \n oui|non")
			#if score>=highscore():
			#	print(" ")
			if choice==("oui"):
				inconnu=10111
				nombreEssais=0
			
