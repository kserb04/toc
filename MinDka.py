import sys


def parse_input():
    skup_stanja = input().strip().split(",")
    simboli_abecede = input().strip().split(",")
    a = input()
    if a:
        prihvatljiva_stanja = a.strip().split(",")
    else:
        prihvatljiva_stanja = []
    pocetno_stanje = input().strip()
    funkcija_prijelaza = {}

    for line in sys.stdin:
        if not line.strip():
            continue
        prvi, drugi = line.strip().split("->")
        trenutno, simbol = prvi.split(",")
        sljedece = drugi
        funkcija_prijelaza[(trenutno, simbol)] = sljedece

    return (
        skup_stanja,
        simboli_abecede,
        prihvatljiva_stanja,
        pocetno_stanje,
        funkcija_prijelaza,
    )


def ispis(tablica, skup_stanja):
    c = 1
    for i in range(1, len(skup_stanja)):
        if c == len(skup_stanja):
            break
        print(skup_stanja[i], end=" -> ")
        for j in range(c):
            print(tablica[i][j], end=" ")

        print()
        c += 1


def ispisD(data_dict):
    for k, v in data_dict.items():
        print(k[0] + "," + k[1] + "->" + v)


def moguce(ind1, ind2, tablica):
    if tablica[ind1][ind2] == 0:
        return True
    else:
        return False


def nedohvatljiva(skup_stanja, prijelazi, pocetno):
    dohvatljiva = []
    dohvatljiva.append(pocetno)
    nova = []
    while True:
        for stanje in skup_stanja:
            c = 0
            if stanje in dohvatljiva:
                for k, v in prijelazi.items():
                    if k[0] == stanje:
                        nova.append(v)
                for novo in nova:
                    if novo not in dohvatljiva:
                        dohvatljiva.append(novo)
                        c = 1
        if c == 0:
            break
    dohvatljiva = sorted(dohvatljiva)

    return dohvatljiva


def isteprih(stanje1, stanje2, prihvatljiva):
    if ((stanje1 in prihvatljiva) and (stanje2 in prihvatljiva)) or (
        (stanje1 not in prihvatljiva) and (stanje2 not in prihvatljiva)
    ):
        return True
    return False


def index(stanje, stanja):
    c = 0
    for i in stanja:
        if i == stanje:
            return c
        else:
            c += 1
    return c


def proba(skup, abeceda, prijelazi, tablica, prihvatljiva, dohvatljiva):
    c = 1
    povezani = {}
    for i in range(1, len(skup)):
        if c == len(skup):
            break
        for j in range(c):
            if tablica[i][j] != 0:
                continue
            for simbol in abeceda:
                count = len(abeceda)

                if prijelazi.get(skup[i], simbol) is not None:
                    slj1 = prijelazi[skup[i], simbol]
                    slj2 = prijelazi[skup[j], simbol]
                    if isteprih(slj1, slj2, prihvatljiva) is not True:
                        tablica[i][j] = 1
                        tablica[j][i] = 1
                    elif slj1 != slj2:
                        if (skup[i], skup[j]) not in povezani.keys():
                            povezani[(skup[i], skup[j])] = []
                        povezani[(skup[i], skup[j])].append((slj1, slj2))

                    else:
                        count -= 1
                elif (prijelazi[skup[i], simbol] not in prijelazi) and (
                    prijelazi[skup[j], simbol] not in prijelazi
                ):
                    count -= 1
                else:
                    break

        c += 1

    pov2 = povezani.copy()
    for i in povezani.keys():
        prvi = index(i[0], dohvatljiva)
        drugi = index(i[1], dohvatljiva)

        if tablica[prvi][drugi] == 1:

            del pov2[i]

    pov3 = {}

    if len(pov2.keys()) != 0:
        for i in pov2.keys():
            i2 = tuple(sorted(i))
            v2 = []
            for j in pov2[i]:
                j2 = tuple(sorted(j))
                v2.append(j2)
            pov3.update({i2: v2})

        for i in pov3.keys():
            for j in pov3[i]:
                if tablica[index(j[0], dohvatljiva)][index(j[1], dohvatljiva)] == 1:
                    i1 = index(i[0], dohvatljiva)
                    i2 = index(i[1], dohvatljiva)
                    tablica[i1][i2] = 1
                    tablica[i2][i1] = 1

    return tablica


def main():
    skup_stanja, abeceda, prihvatljiva, pocetno, prijelazi = parse_input()

    tablica = [[0] * len(skup_stanja) for _ in range(len(skup_stanja))]

    c = 0

    for i in range(len(skup_stanja)):
        c += 1
        if c == len(skup_stanja):
            break
        for j in range(len(skup_stanja)):

            if (
                (skup_stanja[i] in prihvatljiva) and (skup_stanja[j] in prihvatljiva)
            ) or (
                (skup_stanja[i] not in prihvatljiva)
                and (skup_stanja[j] not in prihvatljiva)
            ):
                tablica[i][j] = 0
                tablica[j][i] = 0
            else:
                tablica[i][j] = 1
                tablica[j][i] = 1

    dohvatljiva = nedohvatljiva(skup_stanja, prijelazi, pocetno)

    tablica = proba(dohvatljiva, abeceda, prijelazi, tablica, prihvatljiva, dohvatljiva)

    nova = dohvatljiva.copy()
    for i in range(len(dohvatljiva)):
        for j in range(i):
            if i == j:
                continue
            if tablica[j][i] == 0:
                if dohvatljiva[i] in nova:
                    nova.remove(dohvatljiva[i])
                if dohvatljiva[i] in prihvatljiva:
                    prihvatljiva.remove(dohvatljiva[i])
                    for k, v in prijelazi.items():
                        if v == dohvatljiva[i]:
                            prijelazi[k] = dohvatljiva[j]
                if dohvatljiva[i] == pocetno:
                    pocetno = dohvatljiva[j]

    nova = sorted(nova)
    prih2 = []
    for stanje in prihvatljiva:
        if stanje in nova:
            prih2.append(stanje)

    c = 0
    for stanje in nova:
        if c != 0:
            print(",", end="")
        print(stanje, end="")
        c += 1
    print()

    c = 0
    for slovo in abeceda:
        if c != 0:
            print(",", end="")
        print(slovo, end="")
        c += 1
    print()

    c = 0
    for stanje in prih2:
        if c != 0:
            print(",", end="")
        print(stanje, end="")
        c += 1
    print()

    print(pocetno)
    prijelazi2 = {}
    for k, v in prijelazi.items():
        if k[0] in nova and v in nova:
            prijelazi2[k] = v

    ispisD(prijelazi2)


if __name__ == "__main__":
    main()
