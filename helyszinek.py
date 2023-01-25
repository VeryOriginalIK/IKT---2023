def choice1():
    try:
        choice1 = int(input("1 - Beavatkozol\t\t2 - Kérsz egy sört\t3 - Kimész\n"))
        if choice1 == 1:
            KocsmaVerekedés()
        elif choice1 == 2:
            stamina -= 30
            morale -= 10
        elif choice1 == 3:
            helyszin = input("Válassz, hova mész:\n")
        else:
            print("Nincs ilyen lehetőség!")
            time.sleep(1)
            os.system('cls')
    except:
        choice1()

def Kocsma():
    name = input("Hogy hívnak? ")
    print(f"Épp kinyitod a WC ajtót, amikor egy szék repül el az arcod előtt.\nMegígérted otthon, hogy ma nem verekszel, de a barátaidnak segítség kell.\nMit teszel?")
    choice1()