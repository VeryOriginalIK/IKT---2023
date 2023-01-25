import os
import sys
import time
from mentes import *
questek = {}
inventory = ()
def Jatek():
    try:
        MentesOlvas()
    except:
        name = input("Hogy hívnak? ")
        print(f"Szia, {name}!\n")