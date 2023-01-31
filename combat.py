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

player = Character(name, hp, attack, morale)
enemy = Character(enemy, enemyhp, enemyat, 0)

print("Player's stats:")
print(player.get_stats())

print("Enemy's stats:")
print(enemy.get_stats())

def battle(player, enemy):
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
        print(f"Meghaltál")

battle(player, enemy)
