def main():
    """
    Determina quantos numeros pares de 4 algarismos distintos existem
    """
    alg = "0123456789"
    nmrs = []

    for a1 in alg:
        if a1 != "0": #o primeiro algarismo não pode ser 0
            for a2 in alg:
                if a2 != a1:
                    for a3 in alg:
                        if a3 != a2 and a3 != a1:
                            for a4 in alg:
                                if a4 != a3 and a4 != a1 and a4 != a2 and (int(a4) % 2 == 0):
                                    print("|", a1+a2+a3+a4)
                                    nmrs.append(a1+a2+a3+a4)

    print(len(nmrs))


if __name__ == "__main__":
    main()