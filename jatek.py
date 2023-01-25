import os
import sys
import time
from mentes import *
from helyszinek import *
questek = {}
inventory = {}
hp = 100
stamina = 100
morale = 100
def Jatek():
    try:
        MentesOlvas()
    except:
        Kocsma()