def main():
    """
    Determina quantas capicuas existem entre 2000 e 3999
    """
    alg = "0123456789"
    capicuas = []

    for a1 in alg:
        if a1 == "2" or a1 == "3":  # para que sejam as capicuas entre 2000 e 3999, o primeiro algarismo só pode ser 2 ou 3
            for a2 in alg:          # para que seja capicua, a1=a4 e a2=a3, logo não são definidos.
                print("|", a1+a2+a2+a1) 
                capicuas.append(a1+a2+a2+a1)

    print(len(capicuas))

if __name__ == "__main__":
    main()