from colorama import init
init()
from colorama import Fore, Back, Style


#varriable
mot ="lapins"
motATrouver = ""
i = 0
j = 0
l = 1

#boucle de jeu
motTestee = str(input("donné un mot de 6 lettre ?"))
for i in range (8):
    
    if len(motTestee) == len(mot):
        if motTestee == mot:
            print (Back.YELLOW + mot)
            break
    # test de correspondance lettre 
        elif motTestee != mot:
            if motTestee[j]==mot[0]:
                motATrouver[j] = mot[0]
#                motATrouver[j] = motTestee[Back.YELLOW + j]
            elif motTestee[j]==mot[1]:
                motATrouver[j] = mot[1]
#                motATrouver[1] = motTestee[Back.RED + j]
            elif motTestee[j]==mot[2]:
                motATrouver[j] = mot[2]
#                motATrouver[2] = motTestee[Back.RED + j]
            elif motTestee[j]==mot[3]:
                motATrouver[j] = mot[3]
#                motATrouver[3] = motTestee[Back.RED + j]
            elif motTestee[j]==mot[4]:
                motATrouver[j] = mot[4]
 #               motATrouver[4] = motTestee[Back.RED + j]
            elif motTestee[j]==mot[5]:
                motATrouver[j] = mot[5]
  #              motATrouver[5] = motTestee[Back.RED + j]
            else:
                j=j+1
   #             motATrouver[j] = motTestee[Back.BLUE + j]
    else:
       motTestee = str(input("donné un mot de 6 lettre ?")) 
                    

if motATrouver == mot:
    print("gg")
