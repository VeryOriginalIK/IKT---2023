import os
import sys
import time
import random

questek = {}
fegyver = 0
fegyverDurability = 0
energiaital = 5
hp = 100
stamina = 100
morale = 100
attack = 0
name = ""


#def Mentes(hp, questek, inventory):
        ##Nahajrá Domonkos

#def MentesOlvas():
    ##Nahajrá Domonkos

def irdki(szoveg):
    for i in range(len(szoveg)):
        if i != '\n':
            print(szoveg[i], end='', flush=True); 
            time.sleep(0.015)

def kilep():
    szoveg = "Köszönjük, hogy játszottál."
    irdki(szoveg)
    time.sleep(3)
    sys.exit()
    os.system('cls')
    
def menu():
    os.system('cls')
    szoveg = f"1 - Új játék\t2 - Mentés betöltése\t3 - Kilépés\n"
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
    else:
        menu()

def vege():
    print(f"\n─────────────────────────────────────────────────────────────\n─██████──██████─██████████████─██████████████─██████████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██████████─██░░██████████─\n─██░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────\n─██░░██──██░░██─██░░██████████─██░░██─────────██░░██████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██──██░░██─██░░██████████─\n─██░░░░██░░░░██─██░░██─────────██░░██──██░░██─██░░██─────────\n─████░░░░░░████─██░░██████████─██░░██████░░██─██░░██████████─\n───████░░████───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─────██████─────██████████████─██████████████─██████████████─\n─────────────────────────────────────────────────────────────")
    time.sleep(10)
    menu()

#def harc():
    #Hajrá Donát
class Character:
    def __init__(self, name, hp, morale):
        self.name = name
        self.hp = hp
        self.MR = morale

    def get_stats(self):
        stats = {"Name": self.name,
                 "HP": self.hp,
                 "Moral": self.MR
                 }
        return stats

def battle(player, attack, fightstarter, enemy, fegyver, fegyverNev, fegyverDurability, energiaital):
    szoveg = f"{fightstarter}"
    irdki(szoveg)
    while player.hp > 0 and enemy.hp > 0:
        szoveg = f"Te: {player.hp}\n"
        irdki(szoveg)
        time.sleep(0.1)
        szoveg = f"{enemy.name}: {enemy.hp}\n\n"
        irdki(szoveg)
        time.sleep(0.1)
        szoveg = f"{energiaital} energiaitalod van.\n"
        irdki(szoveg)
        time.sleep(0.2)
        szoveg = "Harc lehetőségek:\n"
        irdki(szoveg)
        szoveg = f"1. Támadás\t\t2. Gyógyítás\n"
        irdki(szoveg)
        choice = input("")
        if choice == "1":
            attack = round((stamina+fegyver+morale)/(random.randrange(1 , 100))*10)
            enemy.hp -= attack
            if attack < 30:
                szoveg = "Hát ez lecsúszott. "
                irdki(szoveg)
            elif 300 > attack > 100:
                szoveg = "Na most jól betaláltál. "
                irdki(szoveg)
            elif attack > 300:
                szoveg = "Hát te aztán nem aprózod el! "
                irdki(szoveg)
            szoveg = f"{attack} életponttal sebezted {enemy.name}-t."
            irdki(szoveg)
            fegyverDurability -= 1
            if fegyverDurability == 0:
                fegyver = 0
                szoveg = f"\nSajnos a harc a {fegyverNev}edet sem kímélte. Széttört {enemy.name} fején."
                irdki(szoveg)
        elif choice == "2":
            if energiaital > 0:    
                player.hp += 100
                energiaital -= 1
                szoveg = "Ittál egy Spar Energy Drinket, a HP-d 100-al nő. "
                irdki(szoveg)
            else:
                szoveg = f"Kifogytál a piából.\n"
                irdki(szoveg)
                attack = round((stamina+fegyver+morale)/(random.randrange(1 , 100))*10)
                enemy.hp -= attack
                szoveg = f"{attack} életponttal sebezted {enemy.name}-t."
                irdki(szoveg)
                fegyverDurability -= 1
            if fegyverDurability == 0:
                fegyver = 0
                szoveg = f"\nA harc a {fegyverNev}edet sem kímélte. Széttört a kezedben, de szerencsére az ökleid még megvannak!"
                irdki(szoveg)
        else:
            szoveg = "nincs ilyen lehetőség.\n"
            irdki(szoveg)

        if enemy.hp > 0:
            enemyattack = round(random.randrange(5, 60))
            player.hp -= enemyattack
            szoveg = f"\n{enemy.name} {enemyattack} -at sebzett rád.\n"
            irdki(szoveg)

    if player.hp > 0:
        szoveg = f" {enemy.name}-nek vége van.\n"
        irdki(szoveg)
    else:
        time.sleep(3)
        szoveg = f"\nMeghaltál :c"
        irdki(szoveg)
        vege()

#sztori kezdete
def Kocsma():
    szoveg = "Hogy hívnak?\n- "
    irdki(szoveg)
    global name
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
            vege()
    elif choice1 == 3:
        return 0
    else:
        Choice1(stamina, morale, sörszam)

def KocsmaItem():
    global fegyver
    global fegyverNev
    global fegyverDurability
    szoveg = f"1 - Felkapod a széket\n2 - Fogsz egy sörösüveget\n3 - Puszta kézzel szállsz be a harcba\n4 - Mégsem akarsz még harcolni\n"
    irdki(szoveg)
    try:
        item1 = int(sys.stdin.readline().strip())
    except:
        szoveg = "Nincs ilyen lehetőség!"
        irdki(szoveg)
        time.sleep(1)
        KocsmaItem()
    if item1 == 1:
        fegyver = 80
        fegyverDurability = 3
        szoveg = "Megfogod a széket a támlájánál, és alig várod, hogy lecsaphass vele valakit. "
        irdki(szoveg)
        fegyverNev = "szék"
    elif item1 == 2:
        fegyver = 40
        fegyverDurability = 8
        szoveg = "A pulthoz csapod az üveged végét, és kész is a bökő. "
        irdki(szoveg)
        fegyverNev = "sörösüveg"
    elif item1 == 3:
        szoveg = "Kemény legény vagy, pár suhancért nem kell fegyverhez nyúlnod. Puszta kézzel szállsz velük harcba. "
        irdki(szoveg)
        fegyverDurability = 500
    elif item1 == 4:
        szoveg = "Ez sosem volt a te tereped. Megrémít az erőszak, meghátrálsz. "
        irdki(szoveg)
        Choice1(stamina, morale, sörszam)

def KocsmaVerekedes():
    szoveg = "Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.\n"
    irdki(szoveg)
    KocsmaItem()
    player = Character(name, hp, morale)
    enemyn = "Győző"
    enemyhp = 200
    szoveg = "A többiek viszont észrevették, hogy be szeretnél szállni a buliba.\n"
    irdki(szoveg)
    time.sleep(0.2)
    fightstarter = f"{enemyn} részegesen feléd ballag.\n"
    time.sleep(0.2)
    enemy = Character(enemyn, enemyhp, 0)
    battle(player, attack, fightstarter, enemy, fegyver, fegyverNev, fegyverDurability, energiaital)
    szoveg = "Sikeresen levertétek Győzőéket, de már nincs kedved tovább maradni."
    irdki(szoveg)

    #1. quest
def KocsmaKijarat(morale):
    szoveg = f"Indulni készülsz. Az ajtóban viszont valaki megállít.\n"
    irdki(szoveg)
    time.sleep(2)
    szoveg = f"-Ha segítesz nekem ígérem megjutalmazlak, de sietnűnk kell!-\n"
    irdki(szoveg)
    time.sleep(2)
    szoveg = f"Suttogja az idegen miközben ide-oda nézeget, mintha keresne valakit."
    irdki(szoveg)
    time.sleep(2)
    szoveg = f"\nMit teszel?\n1 - Elmész az idegenennel\t2 - Félrelököd és kimész\t3 - Visszamész a kocsmába\n"
    irdki(szoveg)
    try:
        helyszin = int(sys.stdin.readline().strip())
    except:
        szoveg = "Nincs ilyen lehetőség!"
        irdki(szoveg)
        time.sleep(1)
        KocsmaKijarat()
    if helyszin == 1:
            ElsoQuest()
    elif helyszin == 2:
            szoveg = f"A falnak csapódik, de egy kést ránt elő a mellénye zsebéből és a hasadba döfi!\n"
            irdki(szoveg)
            time.sleep(2)
            vege()
    elif helyszin == 3:
            szoveg = f"Mindenki a földön vonaglik és jajgatózik. Elrémít a látvány, úgy döntesz mégis az idegennel mész.\n"
            irdki(szoveg)
            morale -= 30
            ElsoQuest()
    time.sleep(1.5)

def ElsoQuest():
    szoveg = f"Követed az idegent a piacra. \n-Ahová mész ott szükséged lesz egy fegyverre!-\n"
    irdki(szoveg)
    time.sleep(2)
    szoveg = f"Odamegy a kovácshoz és egy fényes pengével tér vissza.\n-Tedd el, az első ingyen van!-\n"
    irdki(szoveg)
    time.sleep(2)
    szoveg = f"Mit teszel?\n1 - Elteszed a kardot\t\t2 - Elutasítod az ajándékot\n"
    irdki(szoveg)
    try:
        choice = int(sys.stdin.readline().strip())
    except:
        szoveg = "Nincs ilyen lehetőség!"
        irdki(szoveg)
        time.sleep(1)
    if choice == 1:
        szoveg = f"Elveszed a kardot az idegentől."
        irdki(szoveg)
        time.sleep(1)
        szoveg = f"-Jólvan, kövesd az utat az erdőig. A fák között találsz majd egy ösvényt, az elvezet a helyre ahova menned kell.\nHa találsz ott egy medált kérlek hozd vissza nekem!"
        irdki(szoveg)
    elif choice == 2:
        szoveg = f"Csalódtam benned! Ha ilyen gyáva vagy, akkor menj el!"
        irdki(szoveg)
        time.sleep(1)
        vege()