class Jatekos:
    def __init__(self, questek, fegyver, fegyverDurability, fegyverNev, penz, energiaital, hp, stamina, morale, sörszam, name):
        self.questek = questek
        self.fegyver = fegyver
        self.fegyverDurability = fegyverDurability
        self.fegyverNev = fegyverNev
        self.penz = penz
        self.energiaital = energiaital
        self.hp = hp
        self.stamina = stamina
        self.morale = morale
        self.sörszam = sörszam
        self.name = name

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack