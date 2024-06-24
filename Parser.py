def S(znak, c, flag_1, flag_2, duljina):
    print("S", end="")
    if flag_1 == 1:
        return znak, c, flag_1, flag_2, duljina
    if flag_2 == 1:
        return znak, c, flag_1, flag_2, duljina
    if (znak != "a") and (znak != "b"):
        flag_2 = 1
    else:
        if znak == "a":
            if duljina >= c + 1:
                znak = ulaz[c]
                c += 1
            else:
                znak = 0
                flag_1 = 1
            if flag_2 == 1:
                return znak, c, flag_1, flag_2, duljina
            znak, c, flag_1, flag_2, duljina = A(znak, c, flag_1, flag_2, duljina)
            if flag_2 == 1:
                return znak, c, flag_1, flag_2, duljina
            znak, c, flag_1, flag_2, duljina = B(znak, c, flag_1, flag_2, duljina)
            if flag_2 == 1:
                return znak, c, flag_1, flag_2, duljina
        else:
            if duljina >= c + 1:
                znak = ulaz[c]
                c += 1
            else:
                znak = 0
                flag_1 = 1
            if flag_2 == 1:
                return znak, c, flag_1, flag_2, duljina
            znak, c, flag_1, flag_2, duljina = B(znak, c, flag_1, flag_2, duljina)
            znak, c, flag_1, flag_2, duljina = A(znak, c, flag_1, flag_2, duljina)

    return znak, c, flag_1, flag_2, duljina


def A(znak, c, flag_1, flag_2, duljina):
    print("A", end="")
    if flag_1 == 1:
        return znak, c, flag_1, flag_2, duljina
    if flag_2 == 1:
        return znak, c, flag_1, flag_2, duljina
    if (znak != "b") and (znak != "a"):
        flag_2 = 1
        return znak, c, flag_1, flag_2, duljina
    else:
        if znak == "b":
            if duljina >= c + 1:
                znak = ulaz[c]
                c += 1
            else:
                znak = 0
                flag_1 = 1
                flag_2 = 1
            znak, c, flag_1, flag_2, duljina = C(znak, c, flag_1, flag_2, duljina)
            if flag_2 == 1:
                return znak, c, flag_1, flag_2, duljina
        else:
            if duljina >= c + 1:
                znak = ulaz[c]
                c += 1
            else:
                znak = 0
                flag_1 = 1
    return znak, c, flag_1, flag_2, duljina


def B(znak, c, flag_1, flag_2, duljina):
    print("B", end="")
    if flag_1 == 1:
        return znak, c, flag_1, flag_2, duljina
    if flag_2 == 1:
        return znak, c, flag_1, flag_2, duljina
    if znak == "c":
        if duljina >= c + 1:
            znak = ulaz[c]
            c += 1
        else:
            znak = 0
            flag_1 = 1
        if znak == "c":
            if duljina >= c + 1:
                znak = ulaz[c]
                c += 1
            else:
                znak = 0
                flag_1 = 1
            znak, c, flag_1, flag_2, duljina = S(znak, c, flag_1, flag_2, duljina)
            if znak == "b":
                if duljina >= c + 1:
                    znak = ulaz[c]
                    c += 1
                    if znak == "c":
                        if duljina >= c + 1:
                            znak = ulaz[c]
                            c += 1
                else:
                    znak = 0
                    flag_1 = 1
        else:
            flag_2 = 1

    return znak, c, flag_1, flag_2, duljina


def C(znak, c, flag_1, flag_2, duljina):
    print("C", end="")
    znak, c, flag_1, flag_2, duljina = A(znak, c, flag_1, flag_2, duljina)
    if flag_2 == 1:
        return znak, c, flag_1, flag_2, duljina
    if flag_1 == 1:
        return znak, c, flag_1, flag_2, duljina
    if flag_2 == 1:
        return znak, c, flag_1, flag_2, duljina
    znak, c, flag_1, flag_2, duljina = A(znak, c, flag_1, flag_2, duljina)
    return znak, c, flag_1, flag_2, duljina


def main(znak, c, flag_1, flag_2, duljina):
    znak, c, flag_1, flag_2, duljina = S(znak, c, flag_1, flag_2, duljina)
    if duljina == c:
        if flag_2 == 0:
            print("\nDA")
        else:
            print("\nNE")
    else:
        print("\nNE")


if __name__ == "__main__":
    c = 0
    ulaz = input().strip()
    duljina = len(ulaz)
    if duljina >= c + 1:
        znak = ulaz[c]
        c += 1
    flag_1 = 0
    flag_2 = 0
    main(znak, c, flag_1, flag_2, duljina)
