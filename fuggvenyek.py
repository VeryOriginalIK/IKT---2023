
import os
import sys
import time
questek = {}
fegyver = 0
fegyverDurability = 0
energiaital = 5
hp = 100
stamina = 100
morale = 100
attack = (stamina+morale+fegyver)/10
name = ""


#def Mentes(hp, questek, inventory):
        ##Nahajrá Domonkos

#def MentesOlvas():
    ##Nahajrá Domonkos

def irdki(szoveg):
    for i in range(len(szoveg)):
        print(szoveg[i], end='', flush=True); 
        time.sleep(0.01)
    #  basically animálja a printelést Undertale stílusban, csak a print helyett két sor
    #  szoveg = (megadod a szöveget), aztán kövi sorban meghívod a függvényt a szoveg paraméterrel
    #  egyetlen hátránya (egyelőre a mostani verzióban), hogy \n nem néz ki olyan jól, mintha újra nyomtatod. 

def kilep():
    szoveg = "Köszönjük, hogy játszottál."
    irdki(szoveg)
    time.sleep(3)
    sys.exit()
    os.system('cls')
    

def menu():
    os.system('cls')
    szoveg = f"1 - Új játék\t2 - Mentés betöltés\t3 - Kilépés\n"
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
        kilep()
    

#def harc():
    #Hajrá Donát
class Character:
    def __init__(self, name, hp, atk, morale):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.MR = morale

    def get_stats(self):
        stats = {"Name": self.name,
                 "HP": self.hp,
                 "ATK": self.atk,
                 "Moral": self.MR
                 }
        return stats



def battle(player, enemy, fegyver, fegyverdurability):
    while player.hp > 0 and enemy.hp > 0:
        print("Harc lehetőségek:")
        print("1. Támadás")
        print("2. Gyógyítás")

        choice = input("")

        if choice == "1":
            enemy.hp -= player.atk
            print(f"{name}", player.atk, f"Sebzéz {enemy}-ra/re.")
            fegyverDurability -= 1
            if fegyverDurability == 0:
                fegyver = 0
        elif choice == "2":
            player.hp += 30
            energiaital -= 1
        else:
            print("nincs ilyen lehetőség.")

        if enemy.hp > 0:
            player.hp -= enemy.atk
            print(f"{enemy}", enemy.atk, f"sebzett {name}-ra/re.")

    if player.hp > 0:
        print(f"{name} megnyerte a csatát")
    else:
        print(f"Meghaltál :c")



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
    print(f"                                ____                                     \n                   _           |---||            _                         \n                   ||__________|SSt||___________||                                \n                  /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.                      \n                 /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.                   \n                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.                 \t\t\t\t ____        _____           __                      __ \n               /:.___________________________________\:::`-._             \t\t\t\t/_   |     _/ ____\____     |__| ____ ________ _____/  |_  /\ \n           _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._        \t\t\t\t |   |     \   __\/ __ \    |  |/ __ \\___   // __ \   __\  \/ \n\t_.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._    \t\t\t\t |   |      |  | \  ___/    |  \  ___/ /    /\  ___/|  |   /\  \n\t,'_:._________________________________________________`:_.::::-';`   \t\t\t\t |___| /\   |__|  \___>  \__|  |\____  \\_____ \____ |  |   \/       \n      `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|     \t\t\t\t       \/             \/\______|    \/       \/     |____                 \n       ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||     \t\t\t\t   _____           \n       ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||     \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____     \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__   \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____ \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(   \t\t\t\t /  /_\  \    |  |/ /  _ \_/ ___\ /  ___//     \\__  \  \n       ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|   \t\t\t\t/    |    \   |    <  <_> )  \___ \___ \|  Y Y  \/ __\_ \n    .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |   \t\t\t\t\____|__  /   |__|_ \____/ \_____>_____>|_| |__ (____ /\n     );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-  \t\t\t\t        \/         \/          \/                   \/\n     ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'   \n     ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,           \n     '''''           ''-         ''-         ''-         '''  '''         ")
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
            szoveg =f"\nEgy árokban ébredsz. Nem kellett volna annyit innod. Zúg a fejed. "
            irdki(szoveg)
            time.sleep(3)
            szoveg ="Lassan hazadülöngélsz, már nincs kedved sehova menni."
            irdki(szoveg)
            time.sleep(3)
            print(f"\n─────────────────────────────────────────────────────────────\n─██████──██████─██████████████─██████████████─██████████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██████████─██░░██████████─\n─██░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────\n─██░░██──██░░██─██░░██████████─██░░██─────────██░░██████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██──██░░██─██░░██████████─\n─██░░░░██░░░░██─██░░██─────────██░░██──██░░██─██░░██─────────\n─████░░░░░░████─██░░██████████─██░░██████░░██─██░░██████████─\n───████░░████───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─────██████─────██████████████─██████████████─██████████████─\n─────────────────────────────────────────────────────────────")
            menu()
    #1. quest
    elif choice1 == 3:
        szoveg = f"Indulni készülsz. Az ajtóban valaki megállít.\n"
        irdki(szoveg)
        time.sleep(2)
        szoveg = f"Ha segítesz nekem ígérem megjutalmazlak, de sietnűnk kell!\nSuttogja az idegen miközben ide-oda nézeget, mintha keresne valakit."
        irdki(szoveg)
        szoveg = f"\nMit teszel?\n1 - Elmész az idegenennel\t2 - Félrelököd és kimész\t3 - Visszamész a kocsmába\n"
        irdki(szoveg)
        try:
            helyszin = int(sys.stdin.readline().strip())
        except:
            szoveg = "Nincs ilyen lehetőség!"
            irdki(szoveg)
            time.sleep(1)
        if helyszin == 1:
            szoveg = f"Követed az idegent\n"
            irdki(szoveg)
            ElsoQuest()
        elif helyszin == 2:
            szoveg = f"Az idegen a falnak csapodik, majd egy kést ránt elő a mellénye zsebéből és a hasadba döfi!\n"
            irdki(szoveg)
            time.sleep(2)
            print(f"\n─────────────────────────────────────────────────────────────\n─██████──██████─██████████████─██████████████─██████████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██████████─██░░██████████─\n─██░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────\n─██░░██──██░░██─██░░██████████─██░░██─────────██░░██████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██──██░░██─██░░██████████─\n─██░░░░██░░░░██─██░░██─────────██░░██──██░░██─██░░██─────────\n─████░░░░░░████─██░░██████████─██░░██████░░██─██░░██████████─\n───████░░████───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─────██████─────██████████████─██████████████─██████████████─\n─────────────────────────────────────────────────────────────")
        elif helyszin == 3:
            szoveg = f"Mindenki a földön vonaglik és jajgatózik. Elrémít a látvány, úgy döntesz mégis az idegennel mész.\n"
            irdki(szoveg)
            morale -= 30
            ElsoQuest()

def ElsoQuest():
    szoveg = f"Követed az idegent a piacra. Itt azt mondja:\n-Ahová mész ott szükséged lesz egy kardra!-\nOdamegy a kovácshoz és egy fényes pengével tér vissza.\n-Tedd el, az első ingyen van!"
    irdki(szoveg)
    

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
    if item == 1:
        fegyver = 80
        fegyverDurability = 3
    elif item == 2:
        fegyver = 40
        fegyverDurability = 8
    elif item == 3:
        return 0
    elif item == 4:
        Choice1(stamina, morale, sörszam)
        
def KocsmaVerekedes():
    szoveg = "Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.\n"
    irdki(szoveg)
    KocsmaItem()
    player = Character(name, hp, attack, morale)
    enemyn = "Győző"
    enemyhp = 400
    enemyat = 50
    enemy = Character(enemyn, enemyhp, enemyat, 0)
    battle(player, enemy, fegyver, fegyverDurability)
