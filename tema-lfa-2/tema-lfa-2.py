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
    return alfabet.count('L'), maxx, stariFinale, set(alfabet), dictDFA

def back(stare, k, lmaxx):
    global cuvantCurent, listaCuvinte
    for litera in alfabet:
        if stare in dictDFA.keys():
            for tupluDrumuri in dictDFA[stare]:
                if tupluDrumuri[0] == litera and k < maxx + 1 and lmaxx < (round(1.5 * maxxN) + nr_aparitii_L):
                    if litera == 'L':
                        back(tupluDrumuri[1], k, lmaxx + 1)
                    else:
                        cuvantCurent[k] = tupluDrumuri[0]
                        if tupluDrumuri[1] in stariFinale and k == maxx:
                            listaCuvinte.append(''.join(cuvantCurent))
                        else:
                            back(tupluDrumuri[1], k + 1, lmaxx)

nr_aparitii_L, maxxN, stariFinale, alfabet, dictDFA = citireFisierDFA("tema-lfa-2-DFA-ex6.txt")
stareInitiala = sorted(dictDFA.keys())[0]
listaCuvinte = []

if stareInitiala in stariFinale:
    listaCuvinte.append("cuvant vid")

for maxx in range(maxxN + 1):
    cuvantCurent = [''] * (maxx + 1)
    back(stareInitiala, 1, 1)

listaCuvinte = sorted(set(listaCuvinte))
print('\n'.join(listaCuvinte))
print("nr =", len(listaCuvinte))
