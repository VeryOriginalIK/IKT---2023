import os
import sys
import time
import random

questek = {}
fegyver = 0
fegyverDurability = 0
penz = 0
energiaital = 5
hp = 100
stamina = 100
morale = 100
attack = (stamina+morale+fegyver)/4
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
    irdki("Köszönjük, hogy játszottál.")
    time.sleep(3)
    sys.exit()
    os.system('cls')
    
def menu():
    os.system('cls')
    irdki(f"1 - Új játék\t2 - Mentés betöltés\t3 - Kilépés\n")
    try:
        option = int(sys.stdin.readline().strip())
    except:
        irdki("Nincs ilyen lehetőség!")
        time.sleep(1)
        menu()
    if option == 1:
        Kocsma()
    elif option == 2:
        MentesOlvas()
    elif option == 3:
        kilep()

def vege():
    print(f"\n─────────────────────────────────────────────────────────────\n─██████──██████─██████████████─██████████████─██████████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██████████─██░░██████████─\n─██░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────\n─██░░██──██░░██─██░░██████████─██░░██─────────██░░██████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██──██░░██─██░░██████████─\n─██░░░░██░░░░██─██░░██─────────██░░██──██░░██─██░░██─────────\n─████░░░░░░████─██░░██████████─██░░██████░░██─██░░██████████─\n───████░░████───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─────██████─────██████████████─██████████████─██████████████─\n─────────────────────────────────────────────────────────────")
    time.sleep(2)
    menu()

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

def battle(player, enemy, fegyver, fegyverDurability, energiaital, fightstarter):
    irdki(f"{fightstarter}")
    while player.hp > 0 and enemy.hp > 0:
        irdki(f"Te: {player.hp}\n")
        time.sleep(0.1)
        irdki(f"{enemy.name}: {enemy.hp}\n\n")
        time.sleep(0.1)
        irdki(f"{energiaital} energiaitalod van.\n")
        time.sleep(0.2)
        irdki("Harc lehetőségek:\n")
        irdki(f"1. Támadás\t\t2. Gyógyítás\n")
        choice = input("")
        if choice == "1":
            attack = round((stamina+fegyver+morale)/(random.randrange(1 , 100))*10)
            enemy.hp -= attack
            if attack < 30:
                irdki("Hát ez lecsúszott. ")
            elif 300 > attack > 100:
                irdki("Na most jól betaláltál. ")
            elif attack > 300:
                irdki("Hát te aztán nem aprózod el! ")
            irdki(f"{attack} életponttal sebezted {enemy.name}-t.")
            fegyverDurability -= 1
            if fegyverDurability == 0:
                fegyver = 0
                time.sleep(0.1)
                irdki(f"\nSajnos a harc a {fegyverNev}edet sem kímélte. Széttört {enemy.name} fején.")
        elif choice == "2":
            if energiaital > 0:    
                player.hp += 100
                energiaital -= 1
                irdki("Ittál egy Spar Energy Drinket, a HP-d 100-al nő. ")
            else:
                irdki(f"Kifogytál a piából.\n")
                attack = round((stamina+fegyver+morale)/(random.randrange(1 , 100))*10)
                enemy.hp -= attack
                irdki(f"{attack} életponttal sebezted {enemy.name}-t.")
                fegyverDurability -= 1
            if fegyverDurability == 0:
                fegyver = 0
                irdki(f"\nA harc a {fegyverNev}edet sem kímélte. Széttört a kezedben, de szerencsére az ökleid még megvannak!")
        else:
            irdki("nincs ilyen lehetőség.\n")

        if enemy.hp > 0:
            enemyattack = round(random.randrange(5, 60))
            player.hp -= enemyattack
            irdki(f"\n{enemy.name} {enemyattack} -at sebzett rád.\n")

    if player.hp > 0:
        irdki(f" {enemy.name}-nek vége van.\n")
    else:
        time.sleep(3)
        irdki(f"\nMeghaltál :c")
        vege()

#sztori kezdete
def Kocsma():
    irdki("Hogy hívnak?\n- ")
    global name
    name = sys.stdin.readline().strip()
    irdki(f"Üdv a játékban, {name}. Ajánljuk, hogy a játék elején növeld a képernyőd méretét a neked megfelelőre.\n")
    time.sleep(2.5)
    irdki("Nyugi, megvárunk.")
    time.sleep(2.5)
    os.system('cls')
    print(f"                                ____                                     \n                   _           |---||            _                         \n                   ||__________|SSt||___________||                                \n                  /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.                      \n                 /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.                   \n                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.                 \t\t\t\t ____        _____           __                      __ \n               /:.___________________________________\:::`-._             \t\t\t\t/_   |     _/ ____\____     |__| ____ ________ _____/  |_  /\ \n           _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._        \t\t\t\t |   |     \   __\/ __ \    |  |/ __ \\___   // __ \   __\  \/ \n\t_.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._    \t\t\t\t |   |      |  | \  ___/    |  \  ___/ /    /\  ___/|  |   /\  \n\t,'_:._________________________________________________`:_.::::-';`   \t\t\t\t |___| /\   |__|  \___>  \__|  |\____  \\_____ \____ |  |   \/       \n      `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|     \t\t\t\t       \/             \/\______|    \/       \/     |____                 \n       ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||     \t\t\t\t   _____           \n       ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||     \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____     \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__   \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____ \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(   \t\t\t\t /  /_\  \    |  |/ /  _ \_/ ___\ /  ___//     \\__  \  \n       ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|   \t\t\t\t/    |    \   |    <  <_> )  \___ \___ \|  Y Y  \/ __\_ \n    .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |   \t\t\t\t\____|__  /   |__|_ \____/ \_____>_____>|_| |__ (____ /\n     );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-  \t\t\t\t        \/         \/          \/                   \/\n     ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'   \n     ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,           \n     '''''           ''-         ''-         ''-         '''  '''         ")
    time.sleep(3)
    irdki(f"\nÉpp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted otthon, hogy ma nem verekszel, de a barátaidnak segítség kell.\nMit teszel?")
    Choice1(stamina, morale, sörszam)

sörszam = 0
def Choice1(stamina, morale, sörszam):
    irdki(f"\n1 - Beavatkozol\t\t2 - Kérsz egy sört\t3 - Kimész\n")
    try:
        choice1 = int(sys.stdin.readline().strip())
    except:
        irdki("Nincs ilyen lehetőség!")
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
            irdki(f"Már {sörszam} sört ittál.")
            Choice1(stamina, morale, sörszam)
        else:
            irdki(f"Ez már a 10. sör volt. Forog veled a szoba, majd minden elsötétül.")
            time.sleep(4)
            os.system('cls')
            time.sleep(2)
            for i in range(0,3):
                print('.', end="")
                time.sleep(1)
            time.sleep(1)
            irdki(f"\nEgy árokban ébredsz. Nem kellett volna annyit innod. Zúg a fejed. ")
            time.sleep(3)
            irdki("Lassan hazadülöngélsz, már nincs kedved sehova menni.")
            time.sleep(3)
            vege()
    elif choice1 == 3:
        ElsoQuest()
    time.sleep(1.5)

def ElsoQuest():
    irdki(f"Indulni készülsz. Az ajtóban valaki megállít.\n")
    time.sleep(2)
    irdki(f"-Ha segítesz nekem ígérem megjutalmazlak, de sietnűnk kell!-\n")
    time.sleep(2)
    irdki(f"Suttogja az idegen miközben ide-oda nézeget, mintha keresne valakit.")
    time.sleep(2)
    irdki(f"\nMit teszel?\n1 - Elmész az idegenennel\t2 - Félrelököd és kimész\t3 - Visszamész a kocsmába\n")
    try:
        helyszin = int(sys.stdin.readline().strip())
    except:
        irdki("Nincs ilyen lehetőség!")
        time.sleep(1)
    if helyszin == 1:
        Piac()
    elif helyszin == 2:
            irdki(f"A falnak csapódik, de egy kést ránt elő a mellénye zsebéből és a hasadba döfi!\n")
            time.sleep(2)
            vege()
    elif helyszin == 3:
            irdki(f"Mindenki a földön vonaglik és jajgatózik. Elrémít a látvány, úgy döntesz mégis az idegennel mész.\n")
            morale -= 30
            Piac()

def Piac():
    irdki(f"Követed az idegent a piacra. \n-Ahová mész ott szükséged lesz egy fegyverre!-\n")
    time.sleep(2)
    irdki(f"Odamegy a kovácshoz és egy fényes pengével tér vissza.\n-Tedd el, az első ingyen van!-\n")
    time.sleep(2)
    irdki(f"Mit teszel?\n1 - Elteszed a kardot\t\t2 - Elutasítod az ajándékot\n")
    try:
        choice = int(sys.stdin.readline().strip())
    except:
        irdki("Nincs ilyen lehetőség!")
        time.sleep(1)
    if choice == 1:
        irdki(f"Elveszed a kardot az idegentől.")
        time.sleep(1)
        irdki(f"-Jólvan, kövesd az utat az erdőig. A fák között találsz majd egy ösvényt, az elvezet a helyre ahova menned kell.\nHa találsz ott egy medált kérlek hozd vissza nekem!")
        TutorialBoss()
    elif choice == 2:
        irdki(f"Csalódtam benned! Ha ilyen gyáva vagy, akkor menj el!")
        time.sleep(1)
        vege()

def TutorialBoss():
    time.sleep(4)
    irdki(f"Az eredei út végen egy kopár mezőt találsz. Úgy tűnik senki sincs a közelben, de olyan érzésed van mintha figyelnének.\n")
    time.sleep(2)
    irdki(f"Elindulsz a láda felé amit a pusztaság közepén láttál meg. Mikor már majdnem odaértél rálépsz egy csontra, mej hangos reccsenéssel törik szét a lábad alatt!\n")
    time.sleep(4)
    irdki(f"Hangos üvöltést hallasz a fák közül, a hang az egész testedben félelmet kelt. Már nincs időd elfutni mert egy szörny ront rád, harcolnod kell az életedér!")

    
def KocsmaItem():
    global fegyver
    global fegyverDurability
    global fegyverNev
    irdki(f"1 - Felkapod a széket\n2 - Fogsz egy sörösüveget\n3 - Puszta kézzel szállsz be a harcba\n4 - Mégsem akarsz még harcolni\n")
    try:
        item = int(sys.stdin.readline().strip())
    except:
        irdki("Nincs ilyen lehetőség!")
        time.sleep(1)
        KocsmaItem()
    if item == 1:
        fegyver = 80
        fegyverDurability = 3
        fegyverNev = "szek"
    elif item == 2:
        fegyver = 40
        fegyverDurability = 8
        fegyverNev = "sörösüveg"
        irdki("A pulthoz csapod az üveged végét, és kész is a bökő. ")
    elif item == 3:
        fegyverDurability = 100
        irdki("Kemény legény vagy, pár suhancért nem kell fegyverhez nyúlnod. Puszta kézzel szállsz velük harcba. ")
        return 0
    elif item == 4:
        Choice1(stamina, morale, sörszam)
        
def KocsmaVerekedes():
    irdki("Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.\n")
    KocsmaItem()
    player = Character(name, hp, attack, morale)
    enemyn = "Győző"
    enemyhp = 200
    enemyat = 20
    fightstarter = f"{enemyn} részegesen feléd ballag.\n"
    enemy = Character(enemyn, enemyhp, enemyat, 0)
    battle(player, enemy, fegyver, fegyverDurability, energiaital, fightstarter)
    energiaital += 3
    penz += 800
    irdki("Győzőéket elvertétek, de már nincs kedved ünnepelni. Elveszed kiterült ellenfeledtől 3 energiaitalát, meg találsz nála pár 100ast. Buszjegyre jó lesz.\n")
    ElsoQuest()
