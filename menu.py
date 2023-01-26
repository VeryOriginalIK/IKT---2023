import os
import sys
import time
from jatek import *
from mentes import *
def menu():
    os.system('cls')
    option = 0
    try:
        option = int(input("1 - Új játék\t2 - Játék folytatása\t3 - Kilépés\n"))
    except:
        print("Számot adj meg!")
        time.sleep(1)
        menu()
    if option == 1:
            Jatek()
    elif option == 2:
            SaveOlvas()
    elif option == 3:
            Save()
            sys.exit()
    else:
        print("Nincs ilyen lehetőség!")
        time.sleep(1)
        menu()

menu()