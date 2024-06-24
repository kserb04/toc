def citaj_ulaznu():
    ulazni_nizovi = input().strip().split("|")
    skup_stanja = set(input().strip().split(","))
    ulazni_znakovi = set(input().strip().split(","))
    znakovi_stoga = set(input().strip().split(","))
    prihvatljiva = set(input().strip().split(","))
    pocetno_stanje = input().strip()
    pocetni_znakStoga = input().strip()

    prijelazi = {}
    while True:
        try:
            linija = input().strip()
            if not linija:
                break
            makniStrelicu = linija.strip().split("->")
            lijevo = makniStrelicu[0].split(",")
            desno = makniStrelicu[1].split(",")
            trenutno = lijevo[0]
            ulazni = lijevo[1]
            znakStoga = lijevo[2]
            novo = desno[0]
            nizZnakovaStoga = desno[1]
            prijelazi[(trenutno, ulazni, znakStoga)] = (novo, nizZnakovaStoga)
        except EOFError:
            break

    return (
        ulazni_nizovi,
        skup_stanja,
        ulazni_znakovi,
        znakovi_stoga,
        prihvatljiva,
        pocetno_stanje,
        pocetni_znakStoga,
        prijelazi,
    )


def potisni(pocetno, pocetniNaStogu, ulaz, prijelazi, prihvatljiva, ulazni_nizovi):
    for niz in ulazni_nizovi:
        stog = []
        stog.append(pocetniNaStogu)
        stanje = pocetno
        ispisi(stanje, stog)
        vrh = stog[0]
        niz = niz.split(",")
        while 1:
            provjeri = (stanje, "$", vrh)
            if provjeri in prijelazi.keys():
                novo = prijelazi[provjeri]
                ispisi(novo[0], novo[1])
                stanje = novo[0]
                stog = novo[1]
                vrh = stog[0]
            else:
                break
        duljina = len(niz)
        c = 0
        for u in niz:
            zast = 0
            if (stanje, u[0], vrh) in prijelazi.keys():
                novo = prijelazi[(stanje, u[0], vrh)]
                stog = list(stog)
                novi_stog = izmijeni_stog(stog, novo[1])
                stanje = novo[0]
                vrh = novi_stog[0]
                stog = list(novi_stog)
                ispisi(stanje, stog)
                if stanje in prihvatljiva:
                    znamenka = 1
                else:
                    znamenka = 0
            else:
                provjeri = (stanje, "$", vrh)
                if provjeri in prijelazi.keys():
                    novo = prijelazi[provjeri]
                    stog = list(stog)
                    novi_stog = izmijeni_stog(stog, novo[1])
                    stanje = novo[0]
                    vrh = novi_stog[0]
                    stog = list(novi_stog)
                    ispisi(stanje, stog)
                else:
                    print("fail|", end="")
                    znamenka = 0
                    zast = 1
                    break
                if stanje in prihvatljiva:
                    znamenka = 1
                else:
                    znamenka = 0

            c += 1
            if c == duljina and znamenka == 1:
                break
            else:
                while 1:
                    provjeri = (stanje, "$", vrh)
                    if provjeri in prijelazi.keys():
                        novo = prijelazi[provjeri]
                        stanje = novo[0]
                        stog = list(stog)
                        novi_stog = izmijeni_stog(stog, novo[1])
                        stog = list(novi_stog)
                        vrh = stog[0]
                        ispisi(stanje, stog)
                        if stanje in prihvatljiva:
                            znamenka = 1
                            if c == duljina:
                                break
                        else:
                            znamenka = 0
                    else:
                        break

        if zast == 0:
            print(znamenka)
        else:
            print("0")


def ispisi(stanje, stog):
    print(stanje, end="#")
    for s in stog:
        print(s, end="")
    print("|", end="")


def izmijeni_stog(stog, novo):
    novi = []
    if len(stog) > 1:
        stog.pop(0)
        for n in novo:
            if n == "$":
                continue
            novi.append(n)
        novi.extend(stog)
    else:
        if len(stog) == 1:
            for n in novo:
                if n == "$":
                    continue
                novi.append(n)
        else:
            for n in novo:
                novi.append(n)
    if len(novi) == 0:
        novi.append("$")
    return novi


def main():

    un, ss, uz, zs, p, ps, pzs, prijelazi = citaj_ulaznu()
    potisni(ps, pzs, un[0], prijelazi, p, un)


if __name__ == "__main__":
    main()
