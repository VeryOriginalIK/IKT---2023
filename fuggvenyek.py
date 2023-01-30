import os
import sys
import time
questek = {}
inventory = {}
hp = 100
stamina = 100
morale = 100
helyszin = "kocsma"
name = ""

def menu():
    os.system('cls')
    option = 0
    try:
        option = int(input("1 - Új játék\t2 - Játék folytatása\t3 - Kilépés\n"))
    except:
        print("Számot adj meg!")
        time.sleep(1)
        menu()
    if option == 1:
        Kocsma()
    elif option == 2:
        MentesOlvas()
    elif option == 3:
        Mentes()
        sys.exit()
    else:
        print("Nincs ilyen lehetőség!")
        time.sleep(1)
        menu()

def Mentes(hp, questek, inventory):
    f = open("save.txt", "w", encoding="utf-8")
    f.write(f"{hp}\n{inventory}")
    for key, value in questek.items():
        f.write(f"{key};{value}")
    f.close

#def MentesOlvas():
    ##Nahajrá Domonkos
    

#def harc():
    #Hajrá Donát


#sztori kezdete
def Kocsma():
    name = input("Hogy hívnak? ")
    os.system('cls')
    print(f"Épp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted otthon, hogy ma nem verekszel, de a barátaidnak segítség kell.\nMit teszel?")
    Choice1(stamina, morale, sörszam)

sörszam = 0
def Choice1(stamina, morale, sörszam):
    try:
        choice1 = int(input("1 - Beavatkozol\t\t2 - Kérsz egy sört\t3 - Kimész\n"))
    except:
        Choice1(stamina, morale, sörszam)
    if choice1 == 1:
        KocsmaVerekedes()
        return 0
    elif choice1 == 2:
        if sörszam < 9.5:
            stamina -= 20
            morale -= 10
            sörszam += 1
            print(f"Már {sörszam} sört ittál.")
            Choice1(stamina, morale, sörszam)
        else:
            print("Egy árokban ébredsz. Nem kellett volna annyit innod. Zúg a fejed. Lassan hazadülöngélsz. Anyád szobafogságra ítél, nem mintha amúgy kedved lenne bárhova is menni.\n\t\tVÉGE")
    elif choice1 == 3:
        helyszin = input("Válassz, hova mész:\n")
        #megírni
    else:
        print("Nincs ilyen lehetőség!")
        time.sleep(1)
        os.system('cls')
        Choice1(stamina, morale, sörszam)
        
def KocsmaItem():
    try:
        item = int(input("1 - Felkapod a széket\n2 - Fogsz egy sörösüveget\n3 - Puszta kézzel szállsz be a harcba\n4 - Mégsem akarsz még harcolni\n"))
    except:
        print("Számot adj meg!")
        time.sleep(1)
        KocsmaItem()
    if item == 1:
        inventory["szek"] = 1
    elif item == 2:
        inventory["sorosuveg"] = 1
    elif item == 3:
        return 0
    elif item == 4:
        Choice1(stamina, morale, sörszam)
    else:
        print("Nincs ilyen lehetőség!")
        time.sleep(1)
        KocsmaItem()

def ItemValaszto(helyszin):
    if helyszin == "kocsma":
        KocsmaItem()

def KocsmaVerekedes():
    print("Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.")
    KocsmaItem()
    