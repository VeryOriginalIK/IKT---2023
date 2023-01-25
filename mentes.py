def Mentes(hp, questek, inventory):
    f = open("save.txt", "w", encoding="utf-8")
    f.write(f"{hp}\n{inventory}")
    for key, value in questek.items():
        f.write(f"{key};{value}")
    f.close

def MentesOlvas():
    f = open("save.txt", "r", encoding="utf-8")
    