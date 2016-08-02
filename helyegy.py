#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""2010.majus.11 Informatika emelt szintu erettsegi megoldas.
Adat beinportalast a kovetkezo keppen gondoltam egy szotarban
jegyvasar={hanyadik jegyvasarlas:
{
    "ules szama" :20
    "Felszallas helye": 0
    "Leszallas helye":110
    "Fizetendo osszeg":"ki kell szamolni"
 }

....

}

"""
jegyvasar = {}
n = 0
szamlalo = 0
elso_sor = []
with open("eladott.txt", "rt+", encoding="utf-8") as f:
    for s in f:
        n+=1
        sor = s.replace("\n", "").split(" ")
        if n == 1:
            elso_sor.append(sor[0])
            elso_sor.append(sor[1])
            elso_sor.append(sor[2])
        else:
            szamlalo+=1
            jegyvasar[szamlalo] = {}
            jegyvasar[szamlalo]["Ules szama"] = int(sor[0])
            jegyvasar[szamlalo]["Felszallas helye"] = int(sor[1])
            jegyvasar[szamlalo]["Leszallas helye"] = int(sor[2])
            vav = 0
            jegyar = int(sor[2]) - int(sor[1])
            vav = jegyar / 10
            if jegyar % 10 != 0:
                vav+=1
                hac = int(vav)*int(elso_sor[2])
            else:
                hac = int(vav)*int(elso_sor[2])
            #rounde = int(hac) - int(hac) % 5
            if int(hac) % 5 in [1, 2]:  #lefele kell kerekiteni
                rounded = int(hac) - int(hac) % 5
            elif int(hac) % 5 in [3, 4]:
                rounded = int(hac) + (5 - int(hac) % 5)
            else:
                rounded = int(hac)
            jegyvasar[szamlalo]["Fizetendo osszeg"] = rounded
            
#print(jegyvasar)
print("2. feladat")

""" Meg kell addni az  utolso jegyvasarlo ulesszamat es hogy mennyit utazott"""
print("Ules sorszama:{0} altala megtett km:{1}.".\
      format(jegyvasar[len(jegyvasar)]["Ules szama"],\
             jegyvasar[len(jegyvasar)]["Leszallas helye"]-jegyvasar[len(jegyvasar)]["Felszallas helye"]))


print("3. feladat")
"""Ki kell irni a vegig utazok sorszamat."""
vegig_utazok = []
for k in sorted(jegyvasar.keys()):
    if jegyvasar[k]["Felszallas helye"] == 0 and jegyvasar[k]["Leszallas helye"] == int(elso_sor[1]):
        vegig_utazok.append(str(k))
al = " ".join(vegig_utazok)
print(al)

print("4. feladat")
"""Ossz bevetel meghatarozasa. """
bevetel = 0
for a in jegyvasar.values():
    bevetel+=a["Fizetendo osszeg"]
print("A tarsasagnak a jegybol {} ennyi bevetel szarmazott.".format(bevetel))


print("5. feladat")
"""Kiirni a kepernyore hogy az utolso vegallomas elott hanyan szaltak le es fel osszesen. """
lefel = 0
lehetosegfel = [a["Felszallas helye"] for a in jegyvasar.values()]
lehetosegle = [a["Leszallas helye"] for a in jegyvasar.values()]
lehetoseg = lehetosegfel + lehetosegle

#print(sorted(list(set(lehetoseg))))

for a in jegyvasar.values():
    if a["Felszallas helye"] == sorted(list(set(lehetoseg)))[-2] or a["Leszallas helye"] == sorted(list(set(lehetoseg)))[-2]:
        lefel+=1
print("{} szalltak le es fel az utolso elotti megaloban".format(lefel))

print("6. feladat")
"""Hany helyen alt meg a busz a kiindulas es a vegallomas kozott"""
print("{} helyen all meg a busz a kiindulasi es vegallomas kozott.".format(len(sorted(list(set(lehetoseg))))-2))

print("7. feladat")
"""Kiindulasi pontot be kell kerni a km szam es megnezni hogy az adott pillanatban melyik ulesek uresek es melyikeken ulnek es kogyha
ulnek akkor hanyas szamu utas ul"""

kiindulasi_pont = int(input("Kerem adja meg a kiindulasi pontot hogy hanyadik kilometertol keri az utaslistat: "))
with open("kihol.txt", "wt", encoding="utf-8") as f:

    for ules in range(1, 49):
        ult_e_valaki = False
        for k in sorted(jegyvasar.keys()):
            if jegyvasar[k]["Felszallas helye"] <= kiindulasi_pont and jegyvasar[k]["Leszallas helye"] > kiindulasi_pont \
                and jegyvasar[k]["Ules szama"] == ules:
                f.write(str(ules)+"."+" ules"+":"+str(k)+"."+"utas"+"\n")
                ult_e_valaki = True
        
        if not ult_e_valaki:
            f.write(str(ules)+"."+" ules"+":"+"ures"+"\n")


