import os
import sys
import time
import random
from karakterek import *
import ast

def mentes():
    f = open("mentes.txt", "w", encoding="utf-8")
    f.write(f"{vars(jatekos)}")
    f.close()
    irdki(f"A mentés sikeres. :D\n", "",3)

def betoltes():
    try:
        f = open("mentes.txt", "r", encoding="utf-8")
        for sor in f:
                d = ast.literal_eval(sor)
                values = [v for k, v in d.items()]
                global jatekos
                jatekos = Jatekos(values[0] ,values[1] ,values[2] ,values[3], values[4] ,values[5] ,values[6] ,values[7] ,values[8] ,values[9] ,values[10])
        f.close()
        irdki(f"Mentés betöltve. Üdv a játékban, {jatekos.name}!\n" ,"", 4)
    except:
        irdki("Még nincs mentésed!","", 3)
        menu()

def irdki(szoveg, karakter, sleep):
    if karakter == "segito":
        szoveg = f"\033[92m{szoveg}\033[0m"
    if karakter == "" or karakter == "narrator":
        szoveg = f"\033[1m {szoveg} \033[0m"
    if karakter == "matekt":
        szoveg = f"\033[91m {szoveg} \033[0m"
    #if karakter == "enemy":
    #    szoveg = idk
    if karakter == "anya":
        szoveg = f"\033[94m {szoveg}\033[0m"
    for i in range(len(szoveg)):
        print(szoveg[i], end='', flush=True); 
        time.sleep(0.01)
    time.sleep(sleep)
        
#Először hogy mik közül választhat, majd listába a választható számokat.
#Így nem kell minden lehetőségnél újra beírni
def beker(szoveg, options):
    irdki(szoveg ,"", 0)
    option = 0
    while option not in options:
        option = input("")
        if str(option).upper() == "M":
            mentes()
        if str(option).upper() == "K":
            mentes()
            kilep()
        try:
            option = int(option)
        except:
            pass
        if option not in options:
            irdki(f"Nincs ilyen lehetőség!\n", "", 0)
    return option

def kilep():
    irdki("Köszönjük, hogy játszottál.","", 3)
    sys.exit()
    os.system('cls')
    
def menu():
    os.system('cls')
    option = beker(f"1 - Új játék\t2 - Mentés betöltése\t3 - Kilépés\n",[1, 2, 3])
    if option == 1:
        kar_keszites(Jatekos)   
        Kocsma()
    elif option == 2:
        betoltes()
    elif option == 3:
        kilep()


def vege():
    print(f"\n─────────────────────────────────────────────────────────────\n─██████──██████─██████████████─██████████████─██████████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██████████─██░░██████████─\n─██░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────\n─██░░██──██░░██─██░░██████████─██░░██─────────██░░██████████─\n─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─\n─██░░██──██░░██─██░░██████████─██░░██──██░░██─██░░██████████─\n─██░░░░██░░░░██─██░░██─────────██░░██──██░░██─██░░██─────────\n─████░░░░░░████─██░░██████████─██░░██████░░██─██░░██████████─\n───████░░████───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─\n─────██████─────██████████████─██████████████─██████████████─\n─────────────────────────────────────────────────────────────")
    time.sleep(10)
    menu()
#harcrendszer

def kar_keszites(Jatekos):
    irdki("Hogy hívnak?\n-", "", 0)
    name = sys.stdin.readline().strip()
    global jatekos
    jatekos = Jatekos({} ,0 ,0 ,"" ,0 ,5 ,100 ,100 ,100 ,0 ,name)
    irdki(f"Üdv a játékban, {jatekos.name}!\n","", 2.5)
    irdki(f'Bármikor nyomhatsz "m"-et, ha menteni akarsz, vagy "k"-t a kilépéshez.\n',"", 3)
    irdki("Jó játékot!\n" ,"", 4)
    os.system('cls')


def tamadas():
    attack = round((jatekos.stamina+jatekos.fegyver+jatekos.morale)/(random.randrange(1 , 100))*10)
    enemy.hp -= attack
    if attack < 30:
        irdki("Hát ez lecsúszott. ","", 0)
    elif 300 > attack > 100:
        irdki("Na most jól betaláltál. ","", 0)
    elif attack > 300:
        irdki("Hát te aztán nem aprózod el! ","", 0)
    irdki(f"{attack} életponttal sebezted {enemy.name}-t.", "", 1)
    jatekos.fegyverDurability -= 1
    if jatekos.fegyverDurability == 0:
        irdki(f"\nSajnos a harc a {jatekos.fegyverNev}edet sem kímélte. Széttört {enemy.name} fején.", "", 0.1)
        jatekos.fegyver = 0
        jatekos.fegyverNev = ""


def battle():

    while jatekos.hp > 0 and enemy.hp > 0:
        irdki(f"{jatekos.name}: {jatekos.hp}hp\n","", 0.1)
        irdki(f"{enemy.name}: {enemy.hp}hp\n\n","", 0.1)
        irdki(f"{jatekos.energiaital} energiaitalod van.\n", "",0.2)
        option = beker(f"Harc lehetőségek:\n1. Támadás\t\t2. Gyógyítás\n",[1, 2])
        if option == 1:
            os.system('cls')
            tamadas()
        elif option == 2:
            os.system('cls')
            if jatekos.energiaital > 0:    
                jatekos.hp += 100
                jatekos.energiaital -= 1
                irdki(f"Ittál egy Spar Energy Drinket, a HP-d 100-al nő.", "", 1)
            else:
                irdki(f"Kifogytál a piából.\n", "", 1)
                tamadas()

        if enemy.hp > 0:
            enemy.attack = round(random.randrange(5, 60))
            jatekos.hp -= enemy.attack
            irdki(f"\n{enemy.name} {enemy.attack} -at sebzett rád.\n","", 0)

    if jatekos.hp > 0:
        irdki(f"{enemy.name}-nek vége van.\n","", 0)
    else:
        irdki(f"\nMeghaltál :c","", 3)
        vege()

#sztori kezdete
def Kocsma():
    print(f"                                ____                                     \n                   _           |---||            _                         \n                   ||__________|SSt||___________||                                \n                  /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.                      \n                 /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.                   \n                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.                 \t\t\t\t ____        _____           __                      __ \n               /:.___________________________________\:::`-._             \t\t\t\t/_   |     _/ ____\____     |__| ____ ________ _____/  |_  /\ \n           _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._        \t\t\t\t |   |     \   __\/ __ \    |  |/ __ \\___   // __ \   __\  \/ \n\t_.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._    \t\t\t\t |   |      |  | \  ___/    |  \  ___/ /    /\  ___/|  |   /\  \n\t,'_:._________________________________________________`:_.::::-';`   \t\t\t\t |___| /\   |__|  \___>  \__|  |\____  \\_____ \____ |  |   \/       \n      `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|     \t\t\t\t       \/             \/\______|    \/       \/     |____                 \n       ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||     \t\t\t\t   _____           \n       ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||     \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____     \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__   \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____ \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(   \t\t\t\t /  /_\  \    |  |/ /  _ \_/ ___\ /  ___//     \\__  \  \n       ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|   \t\t\t\t/    |    \   |    <  <_> )  \___ \___ \|  Y Y  \/ __\_ \n    .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |   \t\t\t\t\____|__  /   |__|_ \____/ \_____>_____>|_| |__ (____ /\n     );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-  \t\t\t\t        \/         \/          \/                   \/\n     ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'   \n     ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,           \n     '''''           ''-         ''-         ''-         '''  '''         ",)
    time.sleep(3)
    irdki(f"\nÉpp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted otthon, hogy ma nem verekszel, de a barátaidnak segítség kell.\nMit teszel?","", 2)
    Choice1()

def Choice1():
    option = beker(f"\n1 - Beavatkozol\t\t2 - Kérsz egy sört\t3 - Kimész\n",[1, 2, 3])
    if option == 1:
        KocsmaVerekedes()
    elif option == 2:
        if jatekos.sörszam < 9:
            jatekos.stamina -= 20
            jatekos.morale -= 10
            jatekos.sörszam += 1
            irdki(f"Már {jatekos.sörszam} sört ittál.","", 0)
            Choice1()
        else:
            irdki(f"Ez már a 10. sör volt. Forog veled a szoba, majd minden elsötétül.","", 4)
            os.system('cls')
            for i in range(0,3):
                print('.', end="")
                time.sleep(2)
            irdki(f"\nEgy árokban ébredsz. Nem kellett volna annyit innod. Zúg a fejed. ", "",3)
            irdki("Lassan hazadülöngélsz, már nincs kedved sehova menni.", "",3)
            vege()
    elif option == 3:
        ElsoQuest()

def ElsoQuest():
    irdki(f"Indulni készülsz. Az ajtóban valaki megállít.\n", "",2)
    irdki(f"-Ha segítesz nekem ígérem megjutalmazlak, de sietnünk kell!\n","segito", 2)
    irdki(f"Suttogja az idegen miközben ide-oda nézeget, mintha keresne valakit.","", 2)
    option = beker(f"\nMit teszel?\n1 - Elmész az idegenennel\t2 - Félrelököd és kimész\t3 - Visszamész a kocsmába\n",[1, 2, 3])
    if option == 1:
        Piac()
    elif option == 2:
            irdki(f"A falnak csapódik, de egy kést ránt elő a mellénye zsebéből és a hasadba döfi!\n", "",2)
            vege()
    elif option == 3:
        irdki(f"Mindenki a földön vonaglik és jajgatózik. Elrémít a látvány, úgy döntesz mégis az idegennel mész.\n","", 0)
        jatekos.morale -= 30
        Piac()

def Piac():
    irdki(f"Követed az idegent a piacra.\n","", 1)
    irdki(f'-Ahová mész ott szükséged lesz egy fegyverre!-\n', "segito",2)
    irdki(f"Odamegy a kovácshoz és egy fényes pengével tér vissza.\n-","",1)
    irdki(f"Tedd el, az első ingyen van!-\n","segito", 2)
    option = beker(f"Mit teszel?\n1 - Elteszed a kardot\t\t2 - Elutasítod az ajándékot\n",[1, 2])
    if option == 1:
        jatekos.fegyver = 200
        jatekos.fegyverDurability = 20
        jatekos.fegyverNev = "vajazó kés"
        irdki(f"Elveszed a kardot az idegentől.\n", "",1)
        # szoveg = f"-Jólvan, kövesd az utat az erdőig. A fák között találsz majd egy ösvényt, az elvezet a helyre ahova menned kell.\nHa találsz ott egy medált kérlek hozd vissza nekem!"
        irdki(f'-Jólvan, kövesd az utat az erdőig. A fák között találsz majd egy ösvényt, az elvezet a helyre ahova menned kell.\nHa találsz ott egy medált kérlek hozd vissza nekem!-',"segito", 4)
        # irdki(f"-Jólvan, kövesd az utat az erdőig. A fák között találsz majd egy ösvényt, az elvezet a helyre ahova menned kell.\nHa találsz ott egy medált kérlek hozd vissza nekem!")
        TutorialBoss()
    elif option == 2:
        irdki(f"-Csalódtam benned! Ha ilyen gyáva vagy, akkor menj el!-", "segito", 4)
        vege()

def TutorialBoss():
    irdki(f"\nAz erdei út végen egy kopár mezőt találsz. Úgy tűnik senki sincs a közelben, de olyan érzésed van mintha figyelnének.\n", "", 4)
    irdki(f"Elindulsz a láda felé amit a pusztaság közepén láttál meg. Mikor már majdnem odaértél rálépsz egy csontra, mely hangos reccsenéssel törik szét a lábad alatt!\n","", 4)
    irdki(f"Hangos üvöltést hallasz a fák közül, a hang az egész testedben félelmet kelt. Már nincs időd elfutni mert egy szörny ront rád, harcolnod kell az életedért!\n", "",0)
    global enemy
    enemy = Enemy("", 400, 20)
    battle()
    irdki(f"\nHősies csatában legyőzted a hátborzongató a szörnyet.", "", 2)
    irdki(f"\nkinyitod a ládát és egy nyakláncot találsz benne, amint a kezedbe veszed hirtelen erősebbnek érzed magad.", "", 2)
    irdki(f"\nVissza mész a piacra az idegenhez.", "", 2)
    irdki(f"\nBátor kalandor hát visszatértél és a nyaklánc is megvan", "segito", 2)
    irdki(f"\nNe félj a jutalmadról se feledkeztem meg, tessék itt van 100 arany", "segito", 2)
    jatekos.penz += 100
    Idk()



def Idk():
    irdki(f"\n-Van számodra még egy feladatom! Azt az amulettet gonosz varázslatokkal bűvölték meg, ezért el kell pusztítani!\nMessze a hegyek között van egy vulkán, ott meg lehet semmisíteni,de ez nem olyan egyszerű mint amilyennek hangzik, sokan örzik azt a vulkánt.\nArra kérlek pusztísd el. -\n", "segito", 2)
    option = beker(f"Mit teszel?\n1 - Elviszed az amulettet a vulkánhoz\t\t2 - Inkább odaadod az idegennek\n",[1, 2])
    if option == 1:
        irdki(f"-Köszönöm, hogy segítesz nekem. Tessék egy térkép, így eljuthatsz a vulkánhoz.-", "segito", 4)
        Vulkan()
    elif option == 2:
        irdki(f"-Hát jó. Megértelek.-", "segito", 4)
        time.sleep(1)
        irdki(f"\nMár lassan felkel a nap, egész éjjel az erdőben voltál", "narrator", 4)
        irdki(f"\nAnyukád már halálra aggódta magát", "narrator", 4)
        irdki(f"\nVégre hazaérsz, de anyukád már az ajtóban vár", "narrator", 4)
        irdki(f"\nMit képzelsz magadról egész este nem válaszoltál az üzeneteimre!", "anya", 4)
        irdki(f"\nHalálra aggódtam magam, ezért most egy jó ideig szobafogságban leszel fiatalúr", "anya", 4)
        irdki(f"\nMásnap reggel elmész iskolába", "", 4)
        irdki(f"\nKimerülten ülsz be az iskolapadba, éppen amikor már azt hiszed nem lehet rosszabb, beront a terembe a matek tanár és elkiáltja magát.", "narrator", 4)
        irdki(f"\nDOLGOZAT", "matekt", 4)
        irdki(f"\nAz előző este törtémései miatt teljesen kiment a fejedből és elfeljtettél tanulni", "narrator", 4)
        irdki(f"\nMindenki vegyen elő papírt és tollat, akit puskázáson érek az 1-est kap!", "matekt", 4)


def Vulkan():
    time.sleep(2)
    irdki(f"Az idegentől kapott térkép alapján elindulsz az uticélod felé.\n", "", 2)
    irdki(f"Napok telnek el mire meglátod a tűzhányót, úgy magasodik eléd mint a holnapi matekdoga.\n", "", 2)
    irdki(f"Sok-sok idő után végre ott állsz a hegy lábánál, de még vár rád egy hosszú mászás.", "", 2)
    irdki(f"Végre ott állsz a vulkán tetején, amikor egy kő repül el a fejed mellett.\nMegfordulsz és egy óriási kőszörnyet látsz magad előtt.", "", 2)
    irdki(f"Nekedront és harcolni kezdtek!", "", 2)
    global enemy
    enemy = Enemy("Lánglovag",600, 40)
    battle()
    



def KocsmaItem():
    option = beker(f"1 - Felkapod a széket\n2 - Fogsz egy sörösüveget\n3 - Puszta kézzel szállsz be a harcba\n4 - Mégsem akarsz még harcolni\n",[1, 2, 3 , 4])
    if option == 1:
        jatekos.fegyver = 80
        jatekos.fegyverDurability = 3
        jatekos.fegyverNev = "szék"
    elif option == 2:
        jatekos.fegyver = 40
        jatekos.fegyverDurability = 8
        jatekos.fegyverNev = "sörösüveg"
        irdki("A pulthoz csapod az üveged végét, és kész is a bökő. ","", 0)
    elif option == 3:
        jatekos.fegyverDurability = -1
        irdki("Kemény legény vagy, pár suhancért nem kell fegyverhez nyúlnod. Puszta kézzel szállsz velük harcba. ", "",0)
    elif option == 4:
        Choice1()
        
def KocsmaVerekedes():
    irdki("Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.\n","", 0)
    KocsmaItem()
    global enemy
    enemy = Enemy("Győző",200, 20)
    irdki(f"{enemy.name} részegesen feléd ballag.\n","", 0)
    battle()
    jatekos.energiaital += 3
    jatekos.penz += 800
    irdki("Győzőéket elvertétek, de már nincs kedved ünnepelni. Elveszed kiterült ellenfeledtől 3 energiaitalát, meg találsz nála pár 100ast. Buszjegyre jó lesz.\n","", 2)
    ElsoQuest()
    irdki(f"Indulni készülsz. Az ajtóban valaki megállít.\n","", 2)
    irdki(f"-Ha segítesz nekem ígérem megjutalmazlak, de sietnűnk kell!-\n", "segito",2)
    irdki(f"Suttogja az idegen miközben ide-oda nézeget, mintha keresne valakit.","", 2)
    option = beker(f"\nMit teszel?\n1 - Elmész az idegenennel\t2 - Félrelököd és kimész\t3 - Visszamész a kocsmába\n",[1, 2, 3])
    if option == 1:
        ElsoQuest()
    elif option == 2:
        irdki(f"A falnak csapódik, de egy kést ránt elő a mellénye zsebéből és a hasadba döfi!\n","", 2)
        vege()
    elif option == 3:
        irdki(f"Mindenki a földön vonaglik és jajgatózik. Elrémít a látvány, úgy döntesz mégis az idegennel mész.\n","", 1.5)
        jatekos.morale -= 30
        ElsoQuest()

menu()

# option = beker(f"\nBeledobod a vulkánba az ereklyét\n1 - igen elpusztítom\n2 - megtartod magadnak és használod az erejét",[1, 2, 3])
# if option == 1:

# elif option == 2:
