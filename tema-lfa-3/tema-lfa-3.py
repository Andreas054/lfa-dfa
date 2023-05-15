def citireFisier(numeFisier):
    dict = {}
    with open(numeFisier) as f:
        f = f.read().split('\n')
        while f[-1] == '':
            f = f[:-1]

    for linie in f:
        multimeList = []

        pozDelim = linie.find("->")
        simbol = linie[:pozDelim]
        multimeString = linie[pozDelim + 2:]
        while multimeString.find("/") > 0:
            pozSlash = multimeString.find("/")
            multimeList.append(multimeString[:pozSlash])
            multimeString = multimeString[pozSlash + 1:]

        multimeList.append(multimeString)

        if simbol not in dict:
            dict[simbol] = multimeList

    return dict

def check(dict, cuvant, simbolCurent):
    if cuvant == "":
        for productie in dict[simbolCurent]:
            if productie[0] == "L":
                return True
        return False
    else:
        return checkRecursiv(dict, cuvant, simbolCurent)

def checkRecursiv(dict, cuvant, simbolCurent):
    if cuvant == "":
        for productie in dict[simbolCurent]:
            # if len(productie) < 2:
            if productie[0] == "L":
                return True
        return False
    for productie in dict[simbolCurent]:
        litera = productie[0]
        if len(productie) == 2:
            simbolCurent = productie[1]
            if litera == cuvant[0]:
                if checkRecursiv(dict, cuvant[1:], simbolCurent):
                    return True
        else:
            if litera == cuvant[0] and cuvant[1:] == "":
                return True
    return False

cuvant = input("Cuvant: ")
while cuvant != "0":
    dict = citireFisier("tema-lfa-3-gramatica-ex3.txt")
    print(check(dict, cuvant, "S"), end = "\t")
    print(cuvant)
    cuvant = input("Cuvant: ")

# cuvinte = ["aabbb", "aa", "bbb", "bbbaa", "aaaaaaaabbbbbb", "aaa", "aabbb", "aabbbbbbb", "", "aaaa"]
# cuvinte = ["aa"]
# cuvinte = ["aaaa"]
# dict = citireFisier("tema-lfa-3-gramatica-ex3.txt")
# for cuvant in cuvinte:
#     print(check(dict, cuvant, "S"), end = "\t")
#     print(cuvant)
