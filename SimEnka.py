def read_input():
    ulazni_nizovi = input().strip().split("|")
    skup_stanja = set(input().strip().split(","))
    _ = set(input().strip().split(","))
    _ = set(input().strip().split(","))
    pocetno_stanje = input().strip()
    prijelazi = {}

    while True:
        try:
            linija = input().strip()
            if not linija:
                break
            trenutno, simbol = linija.split("->")[0].split(",")
            skup_iducih_stanja = set(linija.split("->")[1].split(","))
            prijelazi[(trenutno, simbol)] = skup_iducih_stanja
        except EOFError:
            break

    return (
        ulazni_nizovi,
        skup_stanja,
        pocetno_stanje,
        prijelazi,
    )


def nka(
    ulazni_nizovi,
    pocetno_stanje,
    prijelazi,
):
    for ulaz in ulazni_nizovi:
        trenutna_stanja = set()
        sljedeca_stanja = set()
        nova_stanja = set()
        sljedeca_stanja.add(pocetno_stanje)
        eps, added = epsilon_okruzenje(pocetno_stanje, prijelazi)
        if added:
            for state in eps:
                sljedeca_stanja.add(state)
            while added:
                nova_stanja = set()
                nova_stanja, added = epsilon_okr(sljedeca_stanja, prijelazi)
                if nova_stanja.issubset(sljedeca_stanja):
                    break
                sljedeca_stanja.update(nova_stanja)
        output(sljedeca_stanja)

        for simbol in ulaz.split(","):
            count = 0
            print("|", end="")
            trenutna_stanja = sljedeca_stanja
            sljedeca_stanja = set()
            for state in trenutna_stanja:
                nova_stanja = set()
                if prijelazi.get((state, simbol)):
                    count += 1
                    novo = prijelazi.get((state, simbol))
                    sljedeca_stanja.update(novo)
                    eps, added = epsilon_okr(novo, prijelazi)
                    if eps:
                        sljedeca_stanja.update(eps)
                    while added:
                        nova_stanja = set()
                        nova_stanja, added = epsilon_okr(sljedeca_stanja, prijelazi)
                        if nova_stanja.issubset(sljedeca_stanja):
                            break
                        sljedeca_stanja.update(nova_stanja)
            if count == 0:
                sljedeca_stanja.add("#")
            output(sljedeca_stanja)

        print()


def epsilon_okr(states, prijelazi):
    added = False
    okruzenje = set()
    for state in states:
        if prijelazi.get((state, "$")):
            okruzenje.update(prijelazi.get((state, "$")))
            added = True
    return okruzenje, added


def epsilon_okruzenje(state, prijelazi):
    okruzenje = set()
    added = False
    if prijelazi.get((state, "$")):
        okruzenje.update(prijelazi.get((state, "$")))
        added = True
    return okruzenje, added


def output(states):
    c = 0
    prazan = 0
    sortirani = sorted(states)
    for state in sortirani:
        c += 1
        if state == "#":
            prazan += 1
    if prazan != c:
        c = 0
        for state in sortirani:
            if state == "#":
                continue
            if c != 0:
                print(",", end="")
            c += 1
            print(state, end="")
    else:
        print(state, end="")


def main():
    (
        ulazni_nizovi,
        skup_stanja,
        pocetno_stanje,
        prijelazi,
    ) = read_input()
    for state in skup_stanja:
        epsilon_okruzenje(state, prijelazi)
    nka(
        ulazni_nizovi,
        pocetno_stanje,
        prijelazi,
    )


if __name__ == "__main__":
    main()
