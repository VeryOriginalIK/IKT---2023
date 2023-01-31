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

#def Mentes(hp, questek, inventory):
        ##Nahajrá Domonkos

#def MentesOlvas():
    ##Nahajrá Domonkos

def irdki(szoveg):
    for i in range(len(szoveg)):
        print(szoveg[i], end='', flush=True); 
        time.sleep(0.005)

        
    #  basically animálja a printelést Undertale stílusban, csak a print helyett két sor
    #  szoveg = (megadod a szöveget), aztán kövi sorban meghívod a függvényt a szoveg paraméterrel
    #  egyetlen hátránya (egyelőre a mostani verzióban), hogy \n nem néz ki olyan jól, mintha újra nyomtatod. 

def menu():
    os.system('cls')
    szoveg = f"1 - Új játék\t2 - Játék folytatása\t3 - Mentés és kilépés\t4 - Kilépés\n"
    irdki(szoveg)
    try:
        option = int(sys.stdin.readline().strip())
    except:
        szoveg = "Nincs ilyen lehetőség!"
        irdki(szoveg)
        time.sleep(1)
        menu()
    if option == 1:
        Kocsma()
    elif option == 2:
        MentesOlvas()
    elif option == 3:
        Mentes()
        sys.exit()
    elif option == 4:
        sys.exit()
    

#def harc():
    #Hajrá Donát

#sztori kezdete
def Kocsma():
    szoveg = "Hogy hívnak?\n- "
    irdki(szoveg)
    name = sys.stdin.readline().strip()
    szoveg = f"Üdv a játékban, {name}. Ajánljuk, hogy a játék elején növeld a képernyőd méretét a neked megfelelőre.\n"
    irdki(szoveg)
    time.sleep(2.5)
    szoveg = "Nyugi, megvárunk."
    irdki(szoveg)
    time.sleep(2.5)
    os.system('cls')
    print(f"                                ____                                     \n                   _           |---||            _                         \n                   ||__________|SSt||___________||                                \n                  /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.                      \n                 /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.                   \n                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.                 \t\t\t\t ____        _____           __                      __ \n               /:.___________________________________\:::`-._             \t\t\t\t/_   |     _/ ____\____     |__| ____ ________ _____/  |_  /\ \n           _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._        \t\t\t\t |   |     \   __\/ __ \    |  |/ __ \\___   // __ \   __\  \/          \t\t\t\t\t\t_.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._    \t\t\t\t |   |      |  | \  ___/    |  \  ___/ /    /\  ___/|  |   /\  \n\t,'_:._________________________________________________`:_.::::-';`   \t\t\t\t |___| /\   |__|  \___>  \__|  |\____  \\_____ \____ |  |   \/       \n      `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|     \t\t\t\t       \/             \/\______|    \/       \/     |____                 \n       ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||     \t\t\t\t   _____           \n       ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||     \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____     \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__   \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____ \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(   \t\t\t\t /  /_\  \    |  |/ /  _ \_/ ___\ /  ___//     \\__  \  \n       ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|   \t\t\t\t/    |    \   |    <  <_> )  \___ \___ \|  Y Y  \/ __\_ \n    .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |   \t\t\t\t\____|__  /   |__|_ \____/ \_____>_____>|_| |__ (____ /\n     );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-  \t\t\t\t        \/         \/          \/                   \/\n     ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'   \n     ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,           \n     '''''           ''-         ''-         ''-         '''  '''         ")
    time.sleep(3)
    szoveg =f"\nÉpp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted otthon, hogy ma nem verekszel, de a barátaidnak segítség kell.\nMit teszel?"
    irdki(szoveg)
    Choice1(stamina, morale, sörszam)

sörszam = 0
def Choice1(stamina, morale, sörszam):
    szoveg = f"\n1 - Beavatkozol\t\t2 - Kérsz egy sört\t3 - Kimész\n"
    irdki(szoveg)
    try:
        choice1 = int(sys.stdin.readline().strip())
    except:
        szoveg = "Nincs ilyen lehetőség!"
        irdki(szoveg)
        time.sleep(1)
        os.system('cls')
        Choice1(stamina, morale, sörszam)
    if choice1 == 1:
        KocsmaVerekedes()
        return 0
    elif choice1 == 2:
        if sörszam < 9:
            stamina -= 20
            morale -= 10
            sörszam += 1
            szoveg = f"Már {sörszam} sört ittál."
            irdki(szoveg)
            Choice1(stamina, morale, sörszam)
        else:
            szoveg = f"Ez már a 10. sör volt. Forog veled a szoba, majd minden elsötétül."
            irdki(szoveg)
            time.sleep(4)
            os.system('cls')
            time.sleep(2)
            for i in range(0,3):
                print('.', end="")
                time.sleep(1)
            time.sleep(1)
            szoveg =f"\nEgy árokban ébredsz. Nem kellett volna annyit innod. Zúg a fejed."
            irdki(szoveg)
            time.sleep(3)
            szoveg ="Lassan hazadülöngélsz, már nincs kedved sehova menni."
            irdki(szoveg)
            time.sleep(3)
            print(f"\n─────────────────────────────────────────────────────────────\n─██████──██████─██████████████─██████████████─██████████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██████████─██░░██████████─\n─██░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────\n─██░░██──██░░██─██░░██████████─██░░██─────────██░░██████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██──██░░██─██░░██████████─\n─██░░░░██░░░░██─██░░██─────────██░░██──██░░██─██░░██─────────\n─████░░░░░░████─██░░██████████─██░░██████░░██─██░░██████████─\n───████░░████───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─────██████─────██████████████─██████████████─██████████████─\n─────────────────────────────────────────────────────────────")
    elif choice1 == 3:
        szoveg = f"Indulni készülsz. Az ajtóban valaki megállít.\n"
        irdki(szoveg)
        #szoveg = f""
        #1. quest

        #szoveg = f"Válassz, hova mész:\n"
        #irdki(szoveg)
        helyszin = int(sys.stdin.readline().strip())
        #megírni

def KocsmaItem():
    szoveg = f"1 - Felkapod a széket\n2 - Fogsz egy sörösüveget\n3 - Puszta kézzel szállsz be a harcba\n4 - Mégsem akarsz még harcolni\n"
    irdki(szoveg)
    try:
        item = int(sys.stdin.readline().strip())
    except:
        szoveg = "Nincs ilyen lehetőség!"
        irdki(szoveg)
        time.sleep(1)
        KocsmaItem()
    if item.isnumeric == False:
        szoveg = "Számot adj meg!"
        irdki(szoveg)
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
        

def ItemValaszto(helyszin):
    if helyszin == "kocsma":
        KocsmaItem()

def KocsmaVerekedes():
    szoveg = "Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.\n"
    irdki(szoveg)
    KocsmaItem()