def citireFisierDFA(numeFisier):
    dictDFA = {}
    alfabet = []
    with open(numeFisier) as f:
        f = f.read().split('\n')
        while f[-1] == '':
            f = f[:-1]
        stariFinale = f[-1].split()
        maxx = int(f[0])
        for linie in f[1:-1]:
            linie = linie.split()
            alfabet.append(linie[1])
            if linie[0] not in dictDFA.keys():
                dictDFA[linie[0]] = [(linie[1], linie[2])]
            else:
                dictDFA[linie[0]].append((linie[1], linie[2]))
    return maxx, stariFinale, set(alfabet), dictDFA

def afisare(drumCurent):
    print("cuvant = ", end = "")
    for tuplu in drumCurent:
        print(tuplu[0], end = "")
    print("\t;\tdrum = ", end = "")
    for tuplu in drumCurent:
        print(tuplu[1], end=" ")
    print()

def back(stare, k):
    for litera in alfabet:
        for tupluDrumuri in dictDFA[stare]:
            if tupluDrumuri[0] == litera and k < maxx + 1:
                drumCurent[k] = tupluDrumuri
                if tupluDrumuri[1] in stariFinale and k == maxx:
                    afisare(drumCurent)
                else:
                    back(tupluDrumuri[1], k + 1)

#maxx, stariFinale, alfabet, dictDFA = citireFisierDFA("tema-lfa-2-DFA-ex2.txt")
maxx, stariFinale, alfabet, dictDFA = citireFisierDFA("tema-lfa-2-DFA-ex1.txt")

drumCurent = [('', 'q0')] + [0] * maxx
back(drumCurent[0][1], 1)
