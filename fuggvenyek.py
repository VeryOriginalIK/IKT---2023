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
        
#Először hogy mik közül választhat, majd listába a választható számokat.
#Így nem kell minden lehetőségnél újra beírni
def beker(szoveg, options):
    irdki(szoveg)
    option = 0
    while option not in options:
        try:
            option = int(input(""))
        except:
           None
        if option not in options:
            irdki(f"Nincs ilyen lehetőség!\n")
    return option

def kilep():
    irdki("Köszönjük, hogy játszottál.")
    time.sleep(3)
    sys.exit()
    os.system('cls')
    
def menu():
    os.system('cls')
    option = beker(f"1 - Új játék\t2 - Mentés betöltés\t3 - Kilépés\n",[1, 2, 3])
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

#harcrendszer

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
        option = beker(f"Harc lehetőségek:\n1. Támadás\t\t2. Gyógyítás\n",[1, 2])
        if option == 1:
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
        elif option == 2:
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


    
def KocsmaItem():
    global fegyver
    global fegyverDurability
    global fegyverNev
    option = beker(f"1 - Felkapod a széket\n2 - Fogsz egy sörösüveget\n3 - Puszta kézzel szállsz be a harcba\n4 - Mégsem akarsz még harcolni\n",[1, 2, 3 , 4])
    if option == 1:
        fegyver = 80
        fegyverDurability = 3
        fegyverNev = "szék"
    elif option == 2:
        fegyver = 40
        fegyverDurability = 8
        fegyverNev = "sörösüveg"
        irdki("A pulthoz csapod az üveged végét, és kész is a bökő. ")
    elif option == 3:
        fegyverDurability = 100
        irdki("Kemény legény vagy, pár suhancért nem kell fegyverhez nyúlnod. Puszta kézzel szállsz velük harcba. ")
        return 0
    elif option == 4:
        Choice1(stamina, morale, sörszam)
        
def KocsmaVerekedes(morale, energiaital, penz):
    irdki("Úgy döntesz, segítesz barátaidnak, de előtte szükséged lesz egy fegyverre.\n")
    KocsmaItem()
    player = Character(name, hp, attack, 0)
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
    irdki(f"Indulni készülsz. Az ajtóban valaki megállít.\n")
    time.sleep(2)
    irdki(f"-Ha segítesz nekem ígérem megjutalmazlak, de sietnűnk kell!-\n")
    time.sleep(2)
    irdki(f"Suttogja az idegen miközben ide-oda nézeget, mintha keresne valakit.")
    time.sleep(2)
    option = beker(f"\nMit teszel?\n1 - Elmész az idegenennel\t2 - Félrelököd és kimész\t3 - Visszamész a kocsmába\n",[1, 2, 3])
    if option == 1:
        ElsoQuest()
    elif option == 2:
        irdki(f"A falnak csapódik, de egy kést ránt elő a mellénye zsebéből és a hasadba döfi!\n")
        time.sleep(2)
        vege()
    elif option == 3:
        irdki(f"Mindenki a földön vonaglik és jajgatózik. Elrémít a látvány, úgy döntesz mégis az idegennel mész.\n")
        morale -= 30
        ElsoQuest()
        time.sleep(1.5)
