def citireFisierDFA(numeFisier):
    dictDFA = {}
    with open(numeFisier) as f:
        f = f.read().split('\n')
        while f[-1] == '':
            f = f[:-1]
        stariFinale = f[-1].split()
        for linie in f[:-1]:
            linie = linie.split()
            if linie[0] not in dictDFA.keys():
                dictDFA[linie[0]] = [(linie[1], linie[2])]
            else:
                dictDFA[linie[0]].append((linie[1], linie[2]))
    return stariFinale, dictDFA

def citireFisierCuvinte(numeFisier):
    with open(numeFisier) as f:
         f = f.read().split('\n')
         while f[-1] == '':
            f = f[:-1]
    return f

stariFinale, dictDFA = citireFisierDFA("tema-lfa-1-DFA-ex1.txt")
cuvinte = citireFisierCuvinte("tema-lfa-1-cuvinte-ex1.txt")

dictDrumuri = {}

for cuvant in cuvinte:
    drumAles = []
    stareCurenta = sorted(dictDFA.keys())[0]
    for litera in cuvant:
        found = False
        for tuplu in dictDFA[stareCurenta]:
            if tuplu[0] == litera:
                stareCurenta = tuplu[1]
                found = True
                drumAles.append(stareCurenta)
                break
        if found == False:
            break
    else:
        if stareCurenta in stariFinale:
            print("Pentru cuvantul '{}' drumul este ".format(cuvant))
            print(" ".join(drumAles))