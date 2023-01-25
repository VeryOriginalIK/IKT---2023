import os
import sys
import time
def menu():
    os.system('cls')
    option = 0
    try:
        option = int(input("1 - Új játék\t2 - Játék folytatása\t3 - Kilépés\n"))
    except:
        os.system('cls')
        menu()
    if option == 1:
            KarakterGen()
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