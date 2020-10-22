def main():
    """
    Determina quantos numeros exitem maiores do que 9999 e menores que 22000, com os algarismos de 0 a 6;
    """
    alg = "0123456"
    num = []

    for a1 in alg:
        if a1 != 0:
            for a2 in alg:
                for a3 in alg:
                    for a4 in alg:
                        for a5 in alg:
                            if int(a1+a2+a3+a4+a5) < 22000:
                                print("|"+a1+a2+a3+a4+a5)
                                num.append(a1+a2+a3+a4+a5)
    print(len(num))

if __name__ == "__main__":
    main()