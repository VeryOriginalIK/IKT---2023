import os
import time
helyszin = "kocsma"
def Choice1():
    try:
        choice1 = int(input("1 - Beavatkozol\t\t2 - Kérsz egy sört\t3 - Kimész\n"))
    except:
        Choice1()
    if choice1 == 1:
        KocsmaVerekedés()
        return 0
    elif choice1 == 2:
        stamina -= 30
        morale -= 10
    elif choice1 == 3:
        helyszin = input("Válassz, hova mész:\n")
    else:
        print("Nincs ilyen lehetőség!")
        time.sleep(1)
        os.system('cls')
    

def Kocsma():
    name = input("Hogy hívnak? ")
    print(f"Épp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted otthon, hogy ma nem verekszel, de a barátaidnak segítség kell.\nMit teszel?")
    Choice1()

inventory = {}
def KocsmaItem():
    try:
        item = int(input("1 - Felkapod a széket\n2 - Fogsz egy sörösüveget\n3 - Puszta kézzel szállsz be a harcba\n"))
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
    else:
        print("Nincs ilyen lehetőség!")
        time.sleep(1)
        KocsmaItem()

def ItemValaszto():
    if helyszin == "kocsma":
        KocsmaItem()

def KocsmaVerekedés():
    print("Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.")
    KocsmaItem()

