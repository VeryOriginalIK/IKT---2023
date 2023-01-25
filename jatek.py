import os
import sys
import time
from mentes import *
questek = {}
inventory = ()
hp = 100
def Jatek():
    try:
        MentesOlvas()
    except:
        name = input("Hogy hívnak? ")
        print(f"Szia, {name}!\n")