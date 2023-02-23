class Jatekos:
    def __init__(self, questek, fegyver, fegyverDurability, fegyverNev, penz, energiaital, hp, stamina, morale, sörszam, name, questszam):
        self.questek = questek
        self.fegyver = fegyver
        self.fegyverDurability = int(fegyverDurability)
        self.fegyverNev = fegyverNev
        self.penz = int(penz)
        self.energiaital = int(energiaital)
        self.hp = int(hp)
        self.stamina = int(stamina)
        self.morale = int(morale)
        self.sörszam = int(sörszam)
        self.name = name
        self.questszam = questszam

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
