import os
import sys
import time
from mentes import *
questek = {}
inventory = {}
hp = 100
stamina = 100
morale = 100
def Jatek():
    try:
        MentesOlvas()
    except:
        name = input("Hogy hívnak? ")
        print(f"Épp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted a feleségednek, hogy ma nem verekszel, de a barátaid hívnak.\nMit teszel?")
        choice1 = input("1 - Beavatkozol\t2 - Kérsz egy sört\t3 - Kimész")
        if choice1 == 1:
            KocsmaVerekedés ()
        elif choice1 == 2:
            stamina -= 30
            morale -= 10
        elif choice1 == 3:
            Utca()