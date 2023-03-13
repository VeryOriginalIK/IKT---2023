import os
import sys
import time
import random
from karakterek import *
import ast
questek = []
questszam = - 1


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
                jatekos = Jatekos(values[0] ,values[1] ,values[2] ,values[3], values[4] ,values[5] ,values[6] ,values[7] ,values[8] ,values[9] , values[10], values[11], values[12], values[13], values[14])
        f.close()
        irdki(f"Mentés betöltve. Üdv a játékban, {jatekos.name}!\n" ,"", 3)
        os.system('cls')
        time.sleep((1))
        exec(jatekos.questek[jatekos.questszam])
    except:
        irdki("Még nincs mentésed!","", 3)
        menu(questszam)

def irdki(szoveg, karakter, sleep):
    if karakter == "segito":
        szoveg = f"\033[92m{szoveg}\033[0m"
    elif karakter == "" or karakter == "narrator":
        szoveg = f"\033[1m{szoveg}\033[0m"
    elif karakter == "matekt":
        szoveg = f"\033[91m{szoveg}\033[0m"
    elif karakter == "genyo":
        szoveg = f"\033[93m{szoveg}\033[0m"
    elif karakter == "isten":
        szoveg = f"\033[96m{szoveg}\033[0m"
    elif karakter == "te":
        szoveg = f"\033[33m{szoveg}\033[0m]" 
    elif karakter == "police":
        szoveg = f"\033[94m{szoveg}\033[0m"
    elif karakter == "anya":
        szoveg = f"\033[94m{szoveg}\033[0m"
    for i in range(len(szoveg)):
        print(szoveg[i], end='', flush=True)
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
    
def menu(questszam):
    os.system('cls')
    option = beker(f"1 - Új játék\t2 - Mentés betöltése\t3 - Kilépés\n",[1, 2, 3])
    questszam += 1
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
    menu(questszam)

def kar_keszites(Jatekos):
    irdki("Hogy hívnak?\n-", "", 0)
    name = sys.stdin.readline().strip()
    global jatekos
    jatekos = Jatekos(questek ,0 ,0 ,"" ,0 ,5 ,100 ,100 ,100 ,0 ,name, questszam, kuldetes1, kuldetes2, kuldetes3)
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
        irdki(f"\nTe: {jatekos.hp}hp\n","", 0.1)
        irdki(f"{enemy.name}: {enemy.hp}hp\n\n","", 0.1)
        irdki(f"{jatekos.energiaital} energiaitalod van.\n", "",0.2)
        option = beker(f"Harc lehetőségek:\n1. Támadás\t\t2. Gyógyítás\n",[1, 2])
        if option == 1:
            tamadas()
        elif option == 2:
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
        os.system('cls')
        irdki(f" {enemy.name}-nek vége van.\n","", 0)
    else:
        irdki(f"\nMeghaltál :c","", 3)
        vege()

#sztori kezdete
def Kocsma():
    jatekos.questszam +=1
    print(f"                                ____                                     \n                   _           |---||            _                         \n                   ||__________|SSt||___________||                                \n                  /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.                      \n                 /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.                   \n                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.                 \t\t\t\t ____        _____           __                      __ \n               /:.___________________________________\:::`-._             \t\t\t\t/_   |     _/ ____\____     |__| ____ ________ _____/  |_  /\ \n           _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._        \t\t\t\t |   |     \   __\/ __ \    |  |/ __ \\___   // __ \   __\  \/ \n\t_.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._    \t\t\t\t |   |      |  | \  ___/    |  \  ___/ /    /\  ___/|  |   /\  \n\t,'_:._________________________________________________`:_.::::-';`   \t\t\t\t |___| /\   |__|  \___>  \__|  |\____  \\_____ \____ |  |   \/       \n      `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|     \t\t\t\t       \/             \/\______|    \/       \/     |____                 \n       ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||     \t\t\t\t   _____           \n       ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||     \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____     \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__   \t\t\t\t  /  _  \     |  | ______   ____   ______ _____ _____ \n       ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(   \t\t\t\t /  /_\  \    |  |/ /  _ \_/ ___\ /  ___//     \\__  \  \n       ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|   \t\t\t\t/    |    \   |    <  <_> )  \___ \___ \|  Y Y  \/ __\_ \n    .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |   \t\t\t\t\____|__  /   |__|_ \____/ \_____>_____>|_| |__ (____ /\n     );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-  \t\t\t\t        \/         \/          \/                   \/\n     ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'   \n     ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,           \n     '''''           ''-         ''-         ''-         '''  '''         ",)
    time.sleep(3)
    Choice1(False)

def Choice1(kiirt):
    jatekos.questszam +=1
    if kiirt == False:
        irdki(f"\nÉpp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted otthon, hogy ma nem verekszel, de a barátaidnak segítség kell.\nMit teszel?","", 2)
    option = beker(f"\n1 - Beavatkozol\t\t2 - Kérsz egy sört\t3 - Kimész\n",[1, 2, 3])
    if option == 1:
        KocsmaVerekedes()
    elif option == 2:
        if jatekos.sörszam < 9:
            jatekos.stamina -= 20
            jatekos.morale -= 10
            jatekos.sörszam += 1
            irdki(f"Már {jatekos.sörszam} sört ittál.","", 0)
            Choice1(True)
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
    jatekos.questszam +=1
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
    jatekos.questszam +=1
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
        irdki(f'-Jólvan, kövesd az utat az erdőig. A fák között találsz majd egy ösvényt, az elvezet a helyre ahova menned kell.\nHa találsz ott egy medált kérlek hozd vissza nekem!-',"segito", 4)
        TutorialBoss()
    elif option == 2:
        irdki(f"-Hát jó, ha ilyen keménynek érzed magad-", "segito", 4)
        irdki(f'-Jólvan, kövesd az utat az erdőig. A fák között találsz majd egy ösvényt, az elvezet a helyre ahova menned kell.\nHa találsz ott egy medált kérlek hozd vissza nekem!-',"segito", 4)
        TutorialBoss()

def TutorialBoss():
    jatekos.questszam +=1
    irdki(f"\nAz erdei út végen egy kopár mezőt találsz. Úgy tűnik senki sincs a közelben, de olyan érzésed van mintha figyelnének.\n", "", 4)
    irdki(f"Elindulsz a láda felé, amit a pusztaság közepén láttál meg. Mikor már majdnem odaértél rálépsz egy csontra, mely hangos reccsenéssel törik szét a lábad alatt!\n","", 3)
    print(f"                  __,-----,,,,  ,,,--------,__ \n                _-/|\\/|\\/|\\\|\//\\\//|/|//|\\_ \n               /|\/\//\\\\\\\\\\//////////////\\\\ \n             //|//           \\\///           |\\|\ \n            ///|\/             \/               \|\|\ \n           |/|//                                 |\\|\  \n          |/|/                                    \|\|\ \n          ///;    ,,=====,,,  ~~-~~  ,,,=====,,   ;|\|\ \n         |/|/   ''          `'     '"          "'   ;|\| \n         ||/`;   _--~~~~--__         __--~~~~--_   ;/|\|\n         /|||;  :  /       \~~-___-~~/       \  :  ;|\| \n         /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;|| \n         |\|;      ~-____--~'  ; ;  '~--____-~      ;\| \n          ||;            ,`   ;   ;   ',            ;|| \n        __|\ ;        ,'`    (  _  )    `',        ;/|__ \n    _,-~   \|/;    ,'`        ~~ ~~        `',    ;|\   ~-,_ \n  ,'         ||;  '                           '  ;\|/       `, \n , _          ; ,         _--~~-~~--_           ;            _',\n,-' `;-,        ;        ,; |_| | |_| ;,       ;;        ,-;' `-,\n      ; `,      ;       ;_| : `~'~' : |_;       ;      ,' ;\n       ;  `,     ;     :  `\/       \/   :     ;     ,'  ;\n        ;   `,    ;     :               ;     ;    ,'   ;\n         ;    `,_  ;     ;./\_     _/\.;     ;   _,    ;\n      _-'        ;  ;     ~~--|~|~|--~~     ;   ;       '-_\n  _,-'            ;  ;        ~~~~~        ;   ;           `-,_\n,~                 ;  \`~--__         __--~/  ;                ~,\n                    ;   \   ~~-----~~    /   ;                   \n                     ~-_  \  /  |  \   /  _-~                    \n                        ~~-\/   |   \/ -~~                       \n                       (=)=;==========;=(=)")
    irdki(f"Hangos üvöltést hallasz a fák közül, a hang az egész testedben félelmet kelt. Már nincs időd elfutni, mert egy szörny ront rád, harcolnod kell az életedért!\n", "",0)
    global enemy
    enemy = Enemy("", 400, 20)
    battle()
    irdki(f"\nHősies csatában legyőzted a hátborzongató szörnyet.", "", 2)
    jatekos.hp = 100
    irdki(f"\nKinyitod a ládát és egy medált találsz benne, amint a kezedbe veszed hirtelen erősebbnek érzed magad.", "", 2)
    irdki(f"\nVisszamész a piacra az idegenhez.", "", 2)
    irdki(f"\nBátor kalandor, hát visszatértél és a nyaklánc is megvan!", "segito", 2)
    irdki(f"\nNe félj, a jutalmadról se feledkeztem meg, tessék itt van 100 arany.", "segito", 2)
    jatekos.penz += 1000
    Idk()

def Matekdoga():
    jatekos.questszam = 13
    pont = 0
    irdki("\n1.Feladat", "narrator", 2)
    irdki("\nEgy derékszögű háromszőg két befogója 4 és 12 egység hosszúak\nMekkora az átfogó hossza?(Az eredményt 1 tizedesjegyre kerekítve add meg)\n", "", 4)
    valasz = input("")
    if valasz == "12.6":
        pont += 1
    os.system('cls')
    irdki("\n2.Feladat\nMi a rövidítése az alábbi tételnek: \nHa egy szög szárait párhuzamos egyenesekkel metsszük, akkor a párhuzamosokból a szárak által kimetszett szakaszok aránya megegyezik a párhuzamosok által az egyik szárból kimetszett szakaszok arányával?\n", "", 4)        
    valasz = input("")
    if valasz == "psszt":
        pont += 1
    os.system('cls')
    irdki("\n3.Feladat\nÍrd le a szinusz tétel bizonyítását: ", "", 4)
    irdki("\nEsélytelen hogy ezt a feladatot megcsináld! (Túl kicsi az iq szinted)", "", 3)
    irdki(" Beadod a dolgozatot és amikor már indulnál haza a tanár megállít", "", 3)
    irdki(f"\n{jatekos.name}, te maradj csak itt.", "matekt", 3)
    irdki("\n Ez a jegy dönti el, hogy megbuksz-e félévkor. ", "matekt", 3)
    irdki("\nHmm ", "matekt", 3)
    irdki("\nGratulálok, hibátlan dolgozat, de van egy rossz hírem", "matekt", 3)
    irdki("\nEz a jegy így még mindig nem elég, hogy ne bukj meg.", "matekt", 3)
    irdki("\n Ha most el tudod mondani a cosinus tételt, akkor átengedlek", "matekt", 3)
    option = beker(f"\n1 - Megróbálod elmondani a tételt\t2 - Megküzdesz a tanárral",[1, 2])
    if option == 1:
        for i in range(0,3):
            print('.', end="")
            time.sleep(2)
        irdki("\nMiért is próbáltad meg elmondani!? ", "", 3)
        irdki("\nA kínos csendet megszakítja a tanár.", "", 3)
        irdki("\n Holnap már nem is kell bejönnöd, megbuktál.\nMenj a szemem elől!", "matekt", 3)
        irdki("\n A sok stressztől szívrohamot kapsz és a helyszínen meghalsz...", "", 4)
        vege()
    elif option == 2:
        global enemy
        enemy = Enemy("Dr. Csóka Gézáné", 30, 0)
        battle()
        irdki("\nEgy tanuló meglátta, hogy mit tettél a matek tanárral és kihívta a zsarukat", "", 3)
        irdki("\nItt a rendőrség! Azzonal jöjjön ki feltett kézzel, körbe vettük az épületet.", "police", 3)
        option = beker("\n1 - Megadod magad\t2 - Megküzdesz a rendőrökkel",[1, 2])
        if option == 1:
            irdki("\nA rendőrök letartóztattak, és pár héttel később a tárgyaláson 15 év letöltendő börtön bűntetést határoztak meg.", "", 3)
            irdki("\n Nem bírtad sokáig a börtönben, pár év múlva meghaltál, mert megpróbáltál lenyelni egy kést, hogy az őrök ne találják meg.", "", 4)
            vege()
        if option == 2:
            irdki("\n Amint fegyvert rántottál volna, a rendőrök gondolkodás nélkül szitává lőttek.", "", 3)
            vege()    

def Idk():
    jatekos.questszam +=1
    irdki(f"\nDe van számodra még egy feladatom! Azt az amulettet gonosz varázslatokkal bűvölték meg, ezért el kell pusztítani!\nMessze a hegyek között van egy vulkán, ott meg lehet semmisíteni, de ez nem olyan egyszerű mint amilyennek hangzik! Sokan őrzik azt a vulkánt.\nArra kérlek, pusztísd el.\n", "segito", 2)
    option = beker(f"Mit teszel?\n1 - Elviszed az amulettet a vulkánhoz\t\t2 - Inkább odaadod az idegennek\n",[1, 2])
    if option == 1:
        irdki(f"\n-Köszönöm, hogy segítesz nekem. Tessék, egy térkép, így eljuthatsz a vulkánhoz.-", "segito", 2)
        irdki("\n-Még mielőtt továbbmész szeretnél vásárolni tőlem valamit?-", "segito", 2)
        option = beker("\n1 - igen\t2 - nem\n", [1, 2])
        if option == 1:
            irdki("-Van nálam minden mi jó, energiaitaltól elkezdve fegyverekig, de csak egy fegyvert vehetsz-", "segito", 2)
            if jatekos.penz >= 1800:
                option = beker(f"\npénz: {jatekos.penz}\n1 - Axe dezodor(+attack) - 800\n2 - fénykard(++attack) - 1800\n3 - tovább mész\n", [1, 2, 3])
                if option == 1:
                    jatekos.penz -= 800
                    jatekos.fegyver == 300
                    jatekos.fegyverDurability == 40
                    jatekos.fegyverNev == "Axe dezodor"
                    irdki("\n- Tessék adok pár energiaitalt, a ház ajándéka -", "segito", 2)
                    jatekos.energiaital += 5
                    Vulkan()
                elif option == 2:
                    jatekos.penz -= 1800
                    jatekos.fegyver == 500
                    jatekos.fegyverDurability == 70
                    jatekos.fegyverNev == "lézerkard"
                    irdki("\n- Tessék adok pár energiaitalt, a ház ajándéka -", "segito", 2)
                    jatekos.energiaital += 10
                    Vulkan()
                elif option == 3:
                    Vulkan()
            elif jatekos.penz >= 800:
                option = beker(f"\npénz: {jatekos.penz}\n1 - Axe dezodor(+attack) - 800\n2 - tovább mész\n", [1, 2])
                if option == 1:
                    jatekos.penz -= 800
                    jatekos.fegyver == 300
                    jatekos.fegyverDurability == 40
                    jatekos.fegyverNev == "Axe dezodor"
                    irdki("\n- Tessék adok pár energiaitalt, a ház ajándéka -", "segito", 2)
                    jatekos.energiaital += 3
                    Vulkan()
                elif option == 2:
                    Vulkan()
            elif jatekos.penz < 800:
                irdki("\n- Sajnálom de úgy tűnik, hogy nincs elég pénzed semmire, de megesett rajtad a szívem csóri, úgyhogy tessék itt egy energiaital -", "segito", 2)
                jatekos.energiaital += 1
                Vulkan()
        elif option == 2:
            Vulkan()
    elif option == 2:
        irdki(f"\n-Hát jó. Megértelek.-", "segito", 4)
        time.sleep(1)
        irdki(f"\nMár lassan felkel a nap, egész éjjel az erdőben voltál", "narrator", 2)
        irdki(f"\nAnyukád már halálra aggódta magát", "narrator", 2)
        irdki(f"\nVégre hazaérsz, de anyukád már az ajtóban vár", "narrator", 2)
        irdki(f"\nMit képzelsz magadról egész este nem válaszoltál az üzeneteimre!", "anya", 2)
        irdki(f"\nHalálra aggódtam magam, ezért most egy jó ideig szobafogságban leszel fiatalúr", "anya", 2)
        irdki(f"\nMásnap reggel elmész iskolába", "", 2)
        irdki(f"\nKimerülten ülsz be az iskolapadba, éppen amikor már azt hiszed nem lehet rosszabb, beront a terembe a matek tanár és elkiáltja magát.", "narrator", 3)
        irdki(f"\nDOLGOZAT", "matekt", 2)
        irdki(f"\nAz előző este törtémései miatt teljesen kiment a fejedből és elfeljtettél tanulni", "narrator", 2)
        irdki(f"\nMindenki vegyen elő papírt és tollat, akit puskázáson érek az 1-est kap!", "matekt", 2)
        irdki("\nA tanár éppen valamit a az asztalánál keres", "narrator", 2)
        Matekdoga()



def Vulkan():
    jatekos.questszam +=1
    time.sleep(2)
    irdki(f"Az idegentől kapott térkép alapján elindulsz az uticélod felé.\n", "", 2)
    irdki(f"Napok telnek el mire meglátod a tűzhányót, úgy magasodik eléd mint a holnapi matekdoga.\n", "", 2)
    irdki(f"Sok-sok idő után végre ott állsz a hegy lábánál, de még vár rád egy hosszú mászás. ", "", 2)
    irdki(f"Végre ott állsz a vulkán tetején, amikor egy kő repül el a fejed mellett.\nMegfordulsz és egy óriási kőszörnyet látsz magad előtt.\n", "", 2)
    irdki(f" Neked ront és harcolni kezdtek!\n", "", 2)
    global enemy
    enemy = Enemy("Kőpofa",600, 40)
    hp = jatekos.hp
    battle()
    jatekos.h = hp
    global evil
    evil = 0
    irdki(f"Nagyon elfáradtál a harcban, de még nem pihenhetsz, be kell fejezned a feladatot!\n", "", 4)
    irdki(f"Mielőtt befejeznéd a küldetésedet felmerűl benned a kérdés:\n-Miért ne tarthatnám meg? Amikor a kezemben tartom olyan erősnek érzem magam!-\n", "", 4)
    option = beker(f"\nHogyan döntesz?\n1 - Elpusztítod az amulettet\t\t2 - Megtartod az amulettet\n",[1, 2])
    if option == 1:
        irdki(f"\nNem engedsz a kísértésnek, odasétálsz a tűzhányó peremére és teljes erődből a forró lávába halyítod a nyakéket.", "narrator", 2)
        irdki(f"\nLátod ahogy az amulett elmerül a bugyogó anyagban és ez büszkességgel tölt el, végre valami ami sikerült.\nMár éppen elindultál lefele a vulkánról, mikor egy koppanást hallasz, megfordulsz és egy kis csillogó követ veszel észre.", "narrator", 2)
        irdki(f"\nMegpróbálod felvenni a földről, de megégeti a kezed.", "", 2)
        irdki(f"\nRáteríted a pulcsidat és úgy emeled fel, ugyanaz az érzést érzed mint amikor a nyakláncot tartotad a markodban, csak gyengébben.", "", 3)
        irdki(f"\nMiközben hazafelé tartasz eggyátalán nem érzed magad féradtnak, még sohasem voltál ilyen energikus.", "", 2)
        irdki(f"\nFáradság híján mindössze egy napig tart visszaérned a faluba, ahol az idegen már vár.", "", 2)
        irdki(f"\nElmondod neki mit találtál és hogy milyen mágikus képességekkel bír, de ő eggyátalán nem lepődik meg.", "", 2)
        irdki(f"\nÚgy gondolom készíthetnénk neked valamit abbol az anyagból, persze csak ha te is szeretnéd.", "segito", 2)
        irdki(f"\nKét tárgyat tudnék neked készíteni, az egyik megnöveli az életed, a másik az erődet növeli meg.", "segito", 3)
        option = beker(f"\n1 - Hamulett(+hp)\n2 - B.B.oxer(+attack)", [1, 2])
        if option == 1:
            jatekos.hp = 200
            irdki("\nA hamulett olyan mennyiségű bűzzel ruház fel, ami felér egy golyóálló mellénynyel.", "", 2)
        elif option == 2:
            jatekos.fegyver = 100
            jatekos.fegyverDurability = 200
            irdki("\nÚj fegyvereddel könnyedén kiütöd ellenségeid fogsorát", "", 2)
        irdki("\nBátor kalandor, mielőtt még tovább mennénk had mutatkozzak be az én nevem Gáspár Laci.", "segito", 2)
        irdki("\nRöviden az én történetem annyi, hogy bebuktam az énekes szakmát és varázs tárgyak kutatásába kezdtem.", "segito", 2)
        irdki("\nLétezik még három hasonló erővel bíró tárgy, arra kérlek, hogy gyűjtsd őket össze és hozd nekem el, hogy megakadályozzuk, hogy rossz kezekbe kerüljön.", "segito", 2)
        Döntes()
    if option == 2:
        evil = 1
        irdki(f"\nElcsábít a hatalom melyet az amulett nyújt neked, ahelyett, hogy a vulkánba dobnád inkább a nyakadba akasztod.\nAzonnal elárasztja a testedet az erő, még soha nem érezted magad ilyen hatalmasnak!\n", "", 4)
        jatekos.hp = 300
        jatekos.fegyver += 200
        jatekos.fegyverDurability += 1000
        irdki(f"\nVisszamész a piacra az idegenhez", "", 4)
        irdki(f"\n-Féltem, hogy ide jutunk-\n-Azt hittem, hogy elég erős vagy, hogy ellenálj a sötét erők csábításának, de tévedtem-", "segito", 4)
        irdki(f"\n-Adok egy utolsó lehetőséget, hogy megadd magad-", "segito", 4)
        option = beker("\n1 - Megadod magad\t2 - Megküzdesz vele\n", [1, 2])
        if option == 1:
            irdki(f"\nEldobod az amulettet és térde esel\nAz amulett elszívta az összes erődet, mozdulni se bírsz.", "", 2)
            irdki(f"\n-Jól döntöttél {jatekos.name}, de életedet nem kímélhetem meg, túl sok mindent tudsz-", "segito", 2)
            irdki(f"\nAz idegen a saját fegyvereddel öl meg.", "", 4)
            vege()
        elif option == 2:
            irdki(f"\n-Ezt meg fogod bánni-\n", "segito", 4)
            enemy = Enemy("idegen",2000, 80)
            hp = jatekos.hp
            battle()
            jatekos.hp = hp
            jatekos.hp += 50
            jatekos.penz += 1000
            jatekos.energiaital += 20
            irdki(f"\nAz amulett elszívta az áldozatod lelkét, hirtelen erősebbnek érzed magad.", "", 3)
            irdki(f"\nBelenyulsz az idegen zsebébe és egy térképet találsz nála.", "", 2)
            irdki(f"\nNégy misztikus tárgy helyét muatatja a térkép, olyanoknak mint az amuletted.", "", 2)
            irdki(f"\nÚgy döntesz, összegyűjtöd az összeset és leigázod a világot.", "", 4)
            Döntes()

def Heaven():
    if evil == 1:
        jatekos.questszam +=1
        irdki("\nAz elmúlt napok történései után nem fogsz olyan könnyen eljutni a mennybe", "", 2)
        irdki("\nHa egyenesen próbálsz meg bejutni oda fentre azzal mindenkit magadra uszítasz", "", 2)
        irdki("\nDe nincs is nagyon más választásod", "", 2)
        irdki("\nnéhány hét kutatás után rá találtál egy ősi idegen technológiára, ami lehetővé teszi a világok közötti utazást", "", 2)
        irdki("\nEgy barlangban találod magad és ott van előtted a kapu", "", 2)
        irdki("\nDe még mielőtt használni tudnád egy fura kis sárga lény ugrik eléd", "", 2)
        irdki("\nAz amulett nélkül nem értenéd, amit mond de az lefordítja neked", "", 2)
        irdki("\nMár messziről éreztem a sötét aurád", "genyo", 2)
        irdki("\nNem fogom engedni, hogy használd a kaput", "genyo", 2)
        global enemy
        enemy = Enemy("Maykrs", 500, 80)
        hp = jatekos.hp
        battle()
        jatekos.hp = hp
        jatekos.hp += 50
        irdki("\nNem volt nagy kihívás neked", "", 2)
        irdki("\nBeindítod a kaput és átlépsz rajta", "", 2)
        irdki("\nA menny kapui tárulnak eléd, nem is hezitálsz az amulettel felrobbantod a kapukat", "", 2)
        irdki("\nHatalmas pánik tör ki, de neked csak egy célod van megszerezni a mindenható kézigránátot", "", 2)
        irdki("\nVakító fényesség tárul eléd, ami megszólít", "", 2)
        irdki("\nEljött ez a nap is ", "isten", 2)
        irdki("\nA prófécia beteljesedett", "isten", 2)
        irdki("\nRéges régen egy messzi messzi galaxysban megjövendölték, hogy egy nap a bűn megtestesítője eljön és leigázza a világot", "isten", 2)
        irdki("\nHosszú éveken keresztül készültem, hogy megállítsalak", "isten", 2)
        irdki("\nEgy percet se hezitálsz megtámadod Istent", "", 2)
        enemy = Enemy("Isten", 3000, 100)
        hp = jatekos.hp
        battle()
        jatekos.hp = hp
        jatekos.hp += 200
        jatekos.fegyver += 200
        irdki("\nMegölted Istent és a lelkét elszívta az amulett", "", 2)
        irdki("\nMiután eltűnt a teste csak a kézigránát maradt ott", "", 2)
        irdki("\nFelveszed és sietsz el onnan mert Isten nélkül a menny megszűnik létezni", "", 2)
        irdki("\nVisszamész a búvóhelyedre", "", 2)
        Döntes()
    else:
        irdki("\n- Sajnálom, de ahoz, hogy eljuss oda fentre meg kell halnod, de itt ez a totem, ha kész vagy akkor csak törd ketté és máris visszatérsz a testedbe", "segito", 2)
        irdki("\nEz most fájni fog", "segito", 2)
        irdki("\nHatalmas fényesség vesz körül a menny kapui előtt találod magad", "", 2)
        irdki("\nA kapu őr megszólít", "", 2)
        irdki(f"\nÜdv {jatekos.name} gyermekem", "isten", 2)
        irdki("\nFáradj be hosszú utad volt", "isten", 2)
        irdki("\nMerre indulsz el:", "", 2)
        option = beker("\n1 - Templom\n2 - piac\n", [1, 2])
        if option == 1:
            irdki("\nEreklyékkel van tele a templom, de pont amikor elvennéd egy árnyék támad rád hátulról", "", 2)
            enemy = Enemy("árnyharcos", 500, 60)
            hp = jatekos.hp
            battle()
            Hazateres()
        elif option == 2:
            irdki("\nElmész a piacra, ami tele van angyalokkal", "", 2)
            irdki("\nOdamész az egyik standhoz", "", 2)
            irdki("\nÜdvözöllek látom új vagy itt", "isten", 2)
            irdki("\nTessék itt van néhány energiaital a Földről, nálunk minden ingyen van", "isten", 2)
            jatekos.energiaital += 10
            irdki("\nElindulsz a templom felé", "", 4)
            irdki("\nEreklyékkel van tele a templom, de pont amikor elvennéd egy árnyék támad rád hátulról", "", 2)
            enemy = Enemy("árnyharcos", 500, 60)
            hp = jatekos.hp
            battle()
            Hazateres()

def Hazateres():
    irdki("\nAz utolsó ütésdre eltűnik az árnyék", "", 2)
    irdki("\nElveszed a gránátot, majd előveszed a totemet és hazamész", "", 2)
    irdki("\n- látom sikerrel jártál, add ide elpusztítom és már készítem is belőle a fegyvered, apropó fegyver melyiket akarod -", "segito", 2)
    option = beker("\n1 - Mindenható gránát vető\n2 - Szentelt vízből font kevlár mellény",[1, 2])
    if option == 1:
        jatekos.fegyver = 200
        jatekos.fegyverDurability = 100
    elif option == 2:
        hp = jatekos.hp
        hp += 150
        jatekos.hp = hp
    Döntes()

def TapsihapsiLaba():
    jatekos.questszam +=1
    irdki(f"\nA mágikus tárgyak közül Tapsihapsi lábát választottad. Ehhez azonban a Halálcsillagra kell utaznod.", "", 4)
    irdki(f"\nMégis hogyan juthatnál el az űrbe? Hát mi sem egyszerűbb mint szerezni egy űrhajót!", "", 2)
    irdki(f"\nSzerencsédre Elon Musk éppen a Balatonnál tartózkodik, tehát elutazol hozzá és megkéred, hogy adja kölcsön az eggyik rakétáját. ", "", 4)
    irdki(f"\nElon Musk nagyon kedves voltm és felajánlotta a legrégebbi modellt, hogy elutazz vele. ", "", 2)
    irdki(f"\nÚjdonsült rakétatulajdonosként elindulsz a halálcsillag felé, hogy megszerezd a LÁBAT! ", "", 2)
    irdki(f"\nMikor a fémből épített hold közelébe érsz elkapnak, és egy vonósugárral és az 1-es számú hangárba húznak. ", "", 2)
    irdki(f"\nKinézve az űrhajó ablakán egy teljes osztag rohamosztagost látsz, akik feléd menetelnek. ", "", 2)
    irdki(f"\nGyorsan elbújsz a hajó padlójában, hogy ne találjanak meg. A terved sikerül mert senki sem vett észre. ", "", 2)
    irdki(f"\nKiszöksz a rakétából és Tapsihapsi végtagjának keresésére indulsz. ", "", 1)
    print(f"                       .-.\n                      |_:_|\n                     /(_Y_)\\n.                   ( \/M\/ )\n '.               _.'-/'-'\-'._\n   ':           _/.--'[[[[]'--.\_\n     ':        /_'  : |::''| :  '.\\n       ':     //   ./ |oUU| \.'  :\\n         ':  _:'..' \_|___|_/ :   :|\n           ':.  .'  |_[___]_|  :.':\\n            [::\ |  :  | |  :   ; : \\n             '-'   \/'.| |.' \  .;.' |\n             |\_    \  '-'   :       |\n             |  \    \ .:    :   |   |\n             |   \    | '.   :    \  |\n             /       \   :. .;       |\n            /     |   |  :__/     :  \\\n           |  |   |    \:   | \   |   ||\n          /    \  : :  |:   /  |__|   /|\n          |     : : :_/_|  /'._\  '--|_\\n          /___.-/_|-'   \  \\n                         '-'")
    irdki(f"\nSajnos egy nem várt személlyel találkozol menet közben, magával az Uralkodóval! ", "", 2)
    irdki(f"\nA nagyúr felemeli a kezét és elkezd villámokat szorni rád. ", "", 2)
    global enemy
    enemy = Enemy("Uralkodó",2000, 80)
    hp = jatekos.hp
    battle()
    jatekos.hp = hp
    if evil == 1:
        jatekos.hp += 50
    irdki(f"\nHatalmas küzdelmek árán legyőzted az uralkodót, de még nem szerezted meg azt, amiért jöttél, úgyhogy elindulsz megkeresni. ", "", 4)
    irdki(f"\nMerre mész tovább?", "", 2)
    option = beker(f"\n1 - a raktár felé\n2 - a konyha felé\n3 - a börtönök felé", [1, 2, 3])
    if option == 1:
        irdki(f"\nElindulsz a raktár irányába hátha ott találod a mágikus erekjét.", "", 2)
        irdki(f"\nNyitva talállod az ajtót úgyhogy bemész a helyisébe, felkapcsolódik a lámpa és egy zsúfolt szobában talállod magad.", "", 4)
        irdki(f"\nKörbejárod a szobát de nem találsz semmi használhatót, mindössze egy gumikacsát ami valahogyan követ téged.", "", 4)
        irdki(f"\nKimész a raktérből, és máshol keresgélsz tovább.", "", 2)
        irdki("\nMerre mész tovább", "", 2)
        option = beker("\n1- a konyha felé\n2 - a börtönök felé", [1, 2])
        if option == 1:
            irdki("\nAhogyan a konyha felé közeledsz egyre finomabb illatok érik az orrod", "", 2)
            irdki("\nBent nem találsz senkit csak egy 3 fogásos vacsorát", "", 2)
            irdki("\nNem is késlekedsz és evésbe kezdesz", "", 2)
            hp = jatekos.hp
            hp += 100
            irdki("\nA lakoma után sokkal energetikusabbnak érzed magad", "", 2)
            irdki("\nMár csak egy hely maradt, amit még nem néztél meg a börtön", "", 2)
            irdki("\nEgy rohamosztagos örzi a cellákat, mivel elmetrükköt nem tudsz rajta csinálni meg kell küzdened vele", "", 2)
            enemy = Enemy("Rohamosztagos", 400, 20)
            jatekos.hp = hp
            battle()
            jatekos.hp = hp     
            irdki("\nBemész a börtönbe, az egyik cella nyitva van és tapsihapsi van benne láncon", "", 2)
            irdki("\nHapsikám.. te mire.. készülsz...", "isten", 2)
            irdki("\nGondolkodás nélkül levágod gyermekkorod hősének a lábát, aki ebbe belehal", "", 2)
            if evil == 1:
                jatekos.stamina += 500
                irdki("\nAhogy lábadra veszed sokkal gyorabbnak érzed magad", "", 2)
                irdki("\nVisszamész bázisodra", "", 2)
                Döntes()
            else:
                irdki("\nVisszamész a piacra", "", 2)
                irdki("\nGratulálok, viszont van egy rossz hírem ezeknek a maradványait még nem tudom felhasználni, de itt van pár energiaital a fáradozásodért", "segito", 2)
                jatekos.energiaital += 10
                Döntes()
        elif option == 2:
            irdki("\nEgy rohamosztagos örzi a cellákat, mivel elmetrükköt nem tudsz rajta csinálni meg kell küzdened vele", "", 2)
            enemy = Enemy("Rohamosztagos", 400, 20)
            jatekos.hp = hp
            battle()
            jatekos.hp = hp     
            irdki("\nBemész a börtönbe, az egyik cella nyitva van és tapsihapsi van benne láncon", "", 2)
            irdki("\nHapsikám.. te mire.. készülsz...", "isten", 2)
            irdki("\nGondolkodás nélkül levágod gyermekkorod hősének a lábát, aki ebbe belehal", "", 2)
            if evil == 1:
                jatekos.stamina += 500
                irdki("\nAhogy lábadra veszed sokkal gyorabbnak érzed magad", "", 2)
                irdki("\nVisszamész bázisodra", "", 2)
                Döntes()
            else:
                irdki("\nVisszamész a piacra", "", 2)
                irdki("\nGratulálok, viszont van egy rossz hírem ezeknek a maradványait még nem tudom felhasználni, de itt van pár energiaital a fáradozásodért", "segito", 2)
                jatekos.energiaital += 10
                Döntes()
    elif option == 2:
        irdki("\nAhogyan a konyha felé közeledsz egyre finomabb illatok érik az orrod", "", 2)
        irdki("\nBent nem találsz senkit csak egy 3 fogásos vacsorát", "", 2)
        irdki("\nNem is késlekedsz és evésbe kezdesz", "", 2)
        hp = jatekos.hp
        hp += 100
        irdki("\nA lakoma után sokkal energetikusabbnak érzed magad", "", 2)
        irdki("\nMerre mész tovább", "", 2)
        option = beker("\n1- a raktér felé\n2 - a börtönök felé", [1, 2])
        if option == 1:
            irdki(f"\nElindulsz a raktár irányába hátha ott találod a mágikus erekjét.", "", 2)
            irdki(f"\nNyitva talállod az ajtót úgyhogy bemész a helyisébe, felkapcsolódik a lámpa és egy zsúfolt szobában talállod magad.", "", 4)
            irdki(f"\nKörbejárod a szobát de nem találsz semmi használhatót, mindössze egy gumikacsát ami valahogyan követ téged.", "", 4)
            irdki(f"\nKimész a raktérből, és máshol keresgélsz tovább.", "", 2)
            irdki("\nMár csak egy hely maradt, amit még nem néztél meg a börtön", "", 2)
            irdki("\nEgy rohamosztagos örzi a cellákat, mivel elmetrükköt nem tudsz rajta csinálni meg kell küzdened vele", "", 2)
            enemy = Enemy("Rohamosztagos", 400, 20)
            jatekos.hp = hp
            battle()
            jatekos.hp = hp     
            irdki("\nBemész a börtönbe, az egyik cella nyitva van és tapsihapsi van benne láncon", "", 2)
            irdki("\nHapsikám.. te mire.. készülsz...", "isten", 2)
            irdki("\nGondolkodás nélkül levágod gyermekkorod hősének a lábát, aki ebbe belehal", "", 2)
            if evil == 1:
                jatekos.stamina += 500
                irdki("\nAhogy lábadra veszed sokkal gyorabbnak érzed magad", "", 2)
                irdki("\nVisszamész bázisodra", "", 2)
                Döntes()
            else:
                irdki("\nVisszamész a piacra", "", 2)
                irdki("\nGratulálok, viszont van egy rossz hírem ezeknek a maradványait még nem tudom felhasználni, de itt van pár energiaital a fáradozásodért", "segito", 2)
                jatekos.energiaital += 10
                Döntes()
        elif option == 2:
            irdki("\nEgy rohamosztagos örzi a cellákat, mivel elmetrükköt nem tudsz rajta csinálni meg kell küzdened vele", "", 2)
            enemy = Enemy("Rohamosztagos", 400, 20)
            jatekos.hp = hp
            battle()
            jatekos.hp = hp     
            irdki("\nBemész a börtönbe, az egyik cella nyitva van és tapsihapsi van benne láncon", "", 2)
            irdki("\nHapsikám.. te mire.. készülsz...", "isten", 2)
            irdki("\nGondolkodás nélkül levágod gyermekkorod hősének a lábát, aki ebbe belehal", "", 2)
            if evil == 1:
                jatekos.stamina += 500
                irdki("\nAhogy lábadra veszed sokkal gyorabbnak érzed magad", "", 2)
                irdki("\nVisszamész bázisodra", "", 2)
                Döntes()
            else:
                irdki("\nVisszamész a piacra", "", 2)
                irdki("\nGratulálok, viszont van egy rossz hírem ezeknek a maradványait még nem tudom felhasználni, de itt van pár energiaital a fáradozásodért", "segito", 2)
                jatekos.energiaital += 10
                Döntes()
    elif option == 3:
        irdki("\nEgy rohamosztagos örzi a cellákat, mivel elmetrükköt nem tudsz rajta csinálni meg kell küzdened vele", "", 2)
        enemy = Enemy("Rohamosztagos", 400, 20)
        jatekos.hp = hp
        battle()
        jatekos.hp = hp     
        irdki("\nBemész a börtönbe, az egyik cella nyitva van és tapsihapsi van benne láncon", "", 2)
        irdki("\nHapsikám.. te mire.. készülsz...", "isten", 2)
        irdki("\nGondolkodás nélkül levágod gyermekkorod hősének a lábát, aki ebbe belehal", "", 2)
        if evil == 1:
            jatekos.stamina += 500
            irdki("\nAhogy lábadra veszed sokkal gyorabbnak érzed magad", "", 2)
            irdki("\nVisszamész bázisodra", "", 2)
            Döntes()
        else:
            irdki("\nVisszamész a piacra", "", 2)
            irdki("\nGratulálok, viszont van egy rossz hírem ezeknek a maradványait még nem tudom felhasználni, de itt van pár energiaital a fáradozásodért", "segito", 2)
            jatekos.energiaital += 10
            Döntes()
        
def Döntes():
    jatekos.questszam +=1
    if jatekos.kuldetes1 == 0 and jatekos.kuldetes2 == 0 and jatekos.kuldetes3 == 0:
        irdki(f"\nMelyik tárgy levadászására indulsz el?", "", 2)
        option = beker("\n1 - tapsihapsi lába - halálcsillag\n2 - Sanders ezredes kabátja - KFC főhadiszállás\n3 - Mindenható kézigránát - menny\n", [1, 2, 3])
        if option == 1:
            TapsihapsiLaba()
        elif option == 2:
            jatekos.kuldetes2 += 1
            KFC()
        elif option == 3:
            jatekos.kuldetes3 += 1
            Heaven()
    elif jatekos.kuldetes1 == 1 and jatekos.kuldetes2 == 0 and jatekos.kuldetes3 == 0:
        irdki(f"\nMelyik tárgy levadászására indulsz el?", "", 2)
        option = beker("\n1 - Sanders ezredes kabátja - KFC főhadiszállás\n2 - Mindenható kézigránát - menny\n", [1, 2])
        if option == 1:
            jatekos.kuldetes2 += 1
            KFC()
        elif option == 2:
            jatekos.kuldetes3 += 1
            Heaven()
    elif jatekos.kuldetes1 == 0 and jatekos.kuldetes2 == 1 and jatekos.kuldetes3 == 0:
        irdki(f"\nMelyik tárgy levadászására indulsz el?", "", 2)
        option = beker("\n1 - tapsihapsi lába - halálcsillag\n2 - Mindenható kézigránát - menny\n", [1, 2])
        if option == 1:
            jatekos.kuldetes1 += 1
            TapsihapsiLaba()
        elif option == 2:
            jatekos.kuldetes3 += 1
            Heaven()
    elif jatekos.kuldetes1 == 0 and jatekos.kuldetes2 == 0 and jatekos.kuldetes3 == 1:
        irdki(f"\nMelyik tárgy levadászására indulsz el?", "", 2)
        option = beker("\n1 - tapsihapsi lába - halálcsillag\n2 - Sanders ezredes kabátja - KFC főhadiszállás\n", [1, 2])
        if option == 1:
            jatekos.kuldetes1 += 1
            TapsihapsiLaba()
        elif option == 2:
            jatekos.kuldetes2 += 1
            KFC()
    elif jatekos.kuldetes1 == 1 and jatekos.kuldetes2 == 1 and jatekos.kuldetes3 == 0:
        jatekos.kuldetes3 += 1
        Heaven()
    elif jatekos.kuldetes1 == 1 and jatekos.kuldetes2 == 0 and jatekos.kuldetes3 == 1:
        jatekos.kuldetes2 += 1
        KFC()
    elif jatekos.kuldetes1 == 0 and jatekos.kuldetes2 == 1 and jatekos.kuldetes3 == 1:
        jatekos.kuldetes1 += 1
        TapsihapsiLaba()
    elif jatekos.kuldetes1 == 1 and jatekos.kuldetes2 == 1 and jatekos.kuldetes3 == 1:
        Finale()

def Finale():
    if evil == 1:
        irdki(f"\nÖsszegyűjtötted az összes tárgyat, hamarosan te leszel a világ ura, de a semiből egy nagyon ismerős alak ugrik elő.", "", 2)
        irdki(f"\nÁllj meg {jatekos.name}, nem hagyhatom, hogy leigázd a világot! ", "anya", 2)
        irdki(f"\nÉs ezt te mégis, hogy akarod véghez vinni? ", "te", 2)
        irdki(f"\nÉn vagyok a legerősebb a világon, MEGÁLLÍTHATATLAN VAGYOK!!! ", "te", 2)
        irdki(f"\nAzt csak hiszed, én te vagyok egy másik univerzumból, ahol elpusztítottam az amulettet! ", "anya", 2)
        irdki(f"\nAz elpusztított tárgyak darabjaiból egy olyan készüléket készítettünk, ami képes univerzumok között utazni! ", "anya", 2)
        irdki(f"\nAz eddig látott variánsaim közül te vagy a legrosszabb. ", "anya", 2)
        irdki(f"\nÖsszegyűjtöd minden energiád, hogy legyőzd ezt a szélhámost. ", "", 2)
        global enemy
        nev = jatekos.name[::-1]
        enemy = Enemy(nev, 4000, 100)
        battle()
        irdki("\nHatalmas küzdelemben legyőzted magad és elvetted az univerzum ugrót. ", "", 2)
        irdki("\nNem kellett sok idő, hogy uralmad alá vond az egész univerzumot. ", "", 2)
        vege()
    else:
        irdki("\nGratulálok, sikerült mindet összegyűjtened, de küldetésed még nem ér itt véget. ", "segito", 2)
        irdki("\nKészítettem a megmaradt darabokból egy készüléket, aminek a segítségével képes leszel univerzumok között utazni! ", "segito", 2)
        irdki("\nÚti célod a C-117 Föld", "segito", 2)
        irdki("\nEz egy olyan valóság, ahol nem pusztítod el az amulettet és le akarod igázni a világot, le kell győznöd magad. ", "segito", 2)
        irdki("\nSok szerencsét! ", "segito", 2)
        irdki("\nEgy pillanat alatt a másik univerzumban találod magad veled szembe pedig e világi éned. ", "", 2)
        irdki(f"\nÁllj meg {jatekos.name[::-1]}, nem hagyhatom, hogy leigázd a világot! ", "anya", 2)
        irdki(f"\nÉs ezt te mégis, hogy akarod véghez vinni?", "te", 2)
        irdki(f"\nÉn vagyok a legerősebb a világon, MEGÁLLÍTHATATLAN VAGYOK! ", "te", 2)
        irdki(f"\nAzt csak hiszed, én te vagyok egy másik univerzumból, ahol elpusztítottam az amulettet. ", "anya", 2)
        irdki(f"\nAz elpusztított tárgyak darabjaiból egy olyan készüléket készítettünk, ami képes univerzumok között utazni. ", "anya", 2)
        irdki("\nEz a csata dönti el az összes univerzum sorsát!\nGonosz éned nem késlekedik, egyből neked ront.", "", 2)
        nev = jatekos.name[::-1]
        enemy = Enemy(nev, 2000, 80)
        irdki("\nEz lehetetlen..." , "te", 2)
        irdki("\nMiután visszatértél univerzumodba úgy döntesz, hogy járni fogod a világokat és segítesz ahol csak tudsz. ", "", 2)
        irdki("Köszönjük, hogy játszottál!")
        vege()

def KFC():
    jatekos.questszam +=1
    irdki(f"\nElindulsz felkutatni Sanders ezredest, a KFC megalkotóját, hogy eltulajdonítsd tőle a kabátját, ami számodra ismeretlen erővel ruházza fel viselőjét.", "", 2)
    irdki(f"\nEgy hosszú utazás után megtalálod a bázist.", "", 4)
    irdki(f"\nNem gondoltad volna, hogy ennyire védve lesz.", "", 2)
    irdki(f"\nSzerencsére van egy terved.", "", 2)
    irdki(f"\nAzt mondtad az őröknek, hogy elloptad a KFC titkos receptét és szeretnél az ezredessel beszélni.", "", 2)
    irdki(f"\nAz őrök elvezetnek egyenesen az ezredesig.", "", 1)
    print(f"\n⣿⣿⣿⣿⣿⣿⣿⡿⢟⣋⣭⣥⣭⣭⣍⡉⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡏⠁⠠⠶⠛⠻⠿⣿⣿⣿⣿⣷⡄⠄⠄⠄⠄⠉⠻⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠟⠄⢀⡴⢊⣴⣶⣶⣾⣿⣿⣿⣿⢿⡄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿\n⣿⣿⡿⠁⠄⠙⡟⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣎⠃⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿\n⣿⡟⠄⠄⠄⠄⡇⠰⠟⠛⠛⠿⠿⠟⢋⢉⠍⢩⣠⡀⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿\n⣿⠁⠄⠄⠄⠄⠰⠁⣑⣬⣤⡀⣾⣦⣶⣾⣖⣼⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿\n⡏⠄⠄⠄⠄⠄⠄⠄⠨⣿⠟⠰⠻⠿⣣⡙⠿⣿⠋⠄⢀⡀⣀⠄⣀⣀⢀⣀⣀⢸\n⡇⠄⠄⠄⠄⠄⠄⠄⠄⣠⠄⠚⠛⠉⠭⣉⢁⣿⠄⢀⡿⢾⣅⢸⡗⠂⢿⣀⡀⢸\n⡇⠄⠄⠄⠄⠄⠄⠄⠄⠘⢧⣄⠄⣻⣿⣿⣾⠟⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸\n⣿⠄⠄⠄⠄⠄⠄⠄⠄⢠⡀⠄⠄⣿⣿⠟⢁⣴⣿⢸⡄⠄⢦⣤⣤⣤⣤⣄⡀⣼\n⣿⣧⠄⠄⠄⠄⠄⠄⢠⡸⣿⠒⠄⠈⠛⠄⠁⢹⡟⣾⡇⠄⠈⢿⣿⣿⣿⣿⣿⣿\n⣿⣿⣧⣠⣴⣦⠄⠄⢸⣷⡹⣧⣖⡔⠄⠱⣮⣻⣷⣿⣿⠄⠄⠘⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠄⠄⠸⠿⠿⠚⠛⠁⠂⠄⠉⠉⡅⢰⡆⢰⡄⠄⠘⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣷⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⣷⠘⣧⣠⣾⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣄⣀⣀⡀⠄⣀⣀⣹⣦⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿")
    irdki(f"\nAz ezredes kerül veled szembe tábornokával együtt.", "", 2)
    irdki(f"\n- Jól halottam, hogy te vagy az aki ellopta a receptem? -", "matekt", 2)
    irdki(f"\n- Nem is értem miért nem ölettelek meg egyből. Grander tábornok, öld meg! ", "matekt", 2)
    global enemy
    enemy = Enemy("Grander tábornok",750, 50)
    hp = jatekos.hp
    battle()
    jatekos.hp = hp
    if evil == 1:
        jatekos.hp += 50
    irdki("\n- Ez lehetetlen, eddig még senki nem tudta legyőzni! -", "matekt", 2)
    irdki("\n- Mégis mit akarsz tőlem? -", "matekt", 2)
    irdki("\nElmodod neki, hogy a kabátja kell neked, de mielőtt megmagyaráznád félbeszakít.", "", 2)
    irdki("\n- Van egy ajánlatom a számodra. -\n- Megkóstolhatod az új hamburgert és elfelejtük ezt a kis összetűzést. -", "matekt", 2)
    option = beker("\n1 - Elfogadod a hamburgert\n2 - Elveszed a kabátot", [1, 2])
    if option == 1:
        irdki("\n- Jó döntés barátom.", "matekt", 2)
        irdki("\n- Ez itt a ghost dupla grander, el fogod dobni az agyad tőle. ", "matekt", 2)
        irdki("\nSzinte már napok óta nem ettél, ezért percek alatt befalod a hamburgert, de egy kicsit furcsán érzed magad.", "", 2)
        irdki("\n- Tényleg azt hitted, hogy csak úgy elengedlek? Hát téged se az eszedért szeretnek. ", "matekt", 2)
        irdki("\nA hamburgertől annyira meghízol, hogy mozdulni se bírsz.", "", 2)
        irdki("\nSanders lecsap rád K.F.C pengéjével.", "", 2)
        irdki("\n A testedet felhasználják és pár napon belül már téged szolgálnak fel valamelyik étteremben.", "", 3)
        vege()
    elif option == 2:
        irdki("\n- Amúgy is megöltelek volna. ", "matekt", 2)
        enemy = Enemy("Sanders ezredes", 2000, 70)
        hp = jatekos.hp
        battle()
        jatekos.hp = hp
        if evil == 1:
            jatekos.hp += 50
            irdki("\nLeveszed róla kabátját és magadra öltöd. ", "", 2)
            irdki("\nHirtelen még erősebbnek érzed magad. ", "", 2)
            jatekos.hp += 200
            irdki("\nVisszatérsz főhadiszállásodra. ", "", 2)
            Döntes()
        else:
            irdki("\nVisszamész az idegenhez.", "", 2)
            irdki("\n- Á, már vártalak.", "segito", 2)
            irdki("\n- Mivé kovácsoljam Sanders kabátjának maradványait?", "segito", 2)
            option = beker("\n1 - KFC titkos szósz a fegyveredre(+atttack)\n2 - Csirke nyaklánc(+hp)", [1, 2])
            if option == 1:
                jatekos.fegyver += 100
            elif option == 2:
                jatekos.hp += 100
            Döntes()
            
        
def KocsmaItem():
    jatekos.questszam +=1
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
        Choice1(True)
        
def KocsmaVerekedes():
    jatekos.questszam +=1
    irdki("Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.\n","", 0)
    KocsmaItem()
    global enemy
    enemy = Enemy("Győző",200, 20)
    irdki(f"{enemy.name} részegesen feléd ballag.\n","", 0)
    battle()
    jatekos.energiaital += 3
    jatekos.penz += 800
    jatekos.hp = 100
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
        
questek = ["menu(questszam)","Kocsma()","Choice1(False)","KocsmaVerekedes()","ElsoQuest()","Piac()","TutorialBoss()","Idk()","Vulkan()","Döntes()","Heaven()", "KFC()", "TapsihapsiLaba()","Matekdoga()"]
menu(questszam)