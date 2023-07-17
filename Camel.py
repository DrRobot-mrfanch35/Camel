import os
os.system('clear')  # os.system('cls') 
print('\x1b[6;31;40m' + '                                  ---->>> (Appuie sur entrée pour commencer) <<<---- ' + '\x1b[0m')
v12 = input("")
import os
os.system('clear')  # os.system('cls')
print("Bonjour ! Je suis Camel le robot !")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v1 = input("")
import os
os.system('clear')  # os.system('cls')
print("J'aimerais te connaitre, un peu plus.")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v1 = input("")
import os
os.system('clear')  # os.system('cls') 
print("Comment t'appelles tu ?")
print("")
nom = input("Tape ton nom de famille, puis entrée : ")
prenom = input("Tape ton prénom, puis entrée : ")
print("")
import os
os.system('clear')  # os.system('cls') 
print("Bonjour,", prenom, nom,"!")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v6 = input("")
import os
os.system('clear')  # os.system('cls') 
print("Comment vas tu aujourd'hui ? ")
print('\x1b[6;31;40m' + '(ecrit bien ou mal, puis appuie sur entrée)' + '\x1b[0m')
aller = input ("")
import os
os.system('clear')
print ("Tu vas", aller, ", je m'en doutais !")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
Enter02 = input("")
import os
os.system('clear')
age = int(input("Tape ton age puis entrée : "))
print("")
import os
os.system('clear')  # os.system('cls') 
print(age, "ans, t'es trop vieux ,", prenom, nom, "!")
print("")
import os
os.system('clear')  # os.system('cls') 
print("Voyons voir combien de temps, tu as vécu, en nombre de jours, de minutes et de secondes.")
jours = age * 365
minutes = age * 525948     
secondes = age * 31556926
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v7 = input("")
import os
os.system('clear')  # os.system('cls') 
print(prenom, nom, ",t'as vécu", jours,"jours ou", minutes, "minutes ou", secondes, "secondes...")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v9 = input("")
import os
os.system('clear')  # os.system('cls') 
print(prenom, nom, "tu t'es levé", jours, "fois dans ta vie, et tu vas", aller, ". comme d'habitude .")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v8 = input("")
import os
os.system('clear')  # os.system('cls') 
from random import randint
nbr_essais_max = 10
nbr_essais = 1
borne_sup = 100
mon_nombre = randint(1,borne_sup)   # nombre choisi par l'ordinateur
ton_nombre = 0                      # nombre proposÃ© par le joueur
print ("à toi de deviner mon age.")
print("J'ai entre 1 et 100 ans")
print("Tu as",nbr_essais_max,"tentatives au maximum !")
while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:
    print("Essai no ",nbr_essais)
    ton_nombre = int(input("Ta proposition : "))
    if ton_nombre < mon_nombre:
        print("Trop petit")
    elif ton_nombre > mon_nombre:
        print("Trop grand")
    else:
        print("Bravo ! Tu as trouvé",mon_nombre,"ans, en",nbr_essais,"essai(s)")
    nbr_essais += 1
if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :
    print("Désolé, tu utilisé tes",nbr_essais_max,"essais, en vain. T'es nul !")
    print("J'ai",mon_nombre,"ans.")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v1 = input("")
import os
os.system('clear')  # os.system('cls')
print ("Voila, Récapitulons,", prenom, nom, "Tu as", age, "ans, et tu vas", aller, ". Je m'appelle Camel, j'ai", mon_nombre, "ans et je vais toujours très bien.")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v1 = input("")
import os
os.system('clear')  # os.system('cls')
print ("Voila, je te connais un peu mieux, c'est l'heure de ce dire au revoir...")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée) <<<---- ' + '\x1b[0m')
v11 = input("")
import os
os.system('clear')
print("Au revoir,", prenom, nom, ", à bientôt !")
print('\x1b[6;31;40m' + '                                          ---->>> (Appuie sur entrée, pour quitter) <<<---- ' + '\x1b[0m')
v10 = input("")
print("")
print("")
import os
os.system('clear')  # os.system('cls') 

