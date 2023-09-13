#créé par Leonel Akio Briones et Xavier Willoughby
#Jeu de devinette de nombre
#from numpy import *
#from var.txt import score
#from pickle import *
import random
#nombreEssais = 0               
#essai = -1
#score=0
#inconnu = random.randint(0, 1000)    
#print(inconnu)
#highscore=0
#Test du système de sauvegardement qui ne vas probablement pas marcher
#dump(highscore, open("data.txt","wb"))
#d=open("data.txt","r")
#print(d.read())

def jeu_de_devinette():
	nombreEssais = 0               
	essai = -1
	score=0
	inconnu = random.randint(0, 1000)    
	print(inconnu)
	highscore=0
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
			else:
				score += 1
				#le text qui apparait quand la réponse est bonne
				print("\n\nBravo! Votre score est : %d"%score)
				choice=input("\n Voulez vous recomencer: \n oui|non\n")
				#if score>=highscore():
				#	print(" ")
				if choice==("oui"):
					jeu_de_devinette()
			
jeu_de_devinette()



