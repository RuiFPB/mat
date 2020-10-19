def main():
    """
    Determina quantos numeros de 4 algarismos, menores que 5000 e divisiveis por 5 existem, apenas com os algarismos 2,3,4,5
    """
    alg = "2345"
    nmrs = []

    for a1 in alg:
        if a1 != "5": #para ser menor que 5000, o primeiro algarismo não pode ser 5
            for a2 in alg:
                for a3 in alg:
                    for a4 in alg:
                        if a4 == "5": #para ser divisivel por 5, o ultimo algarismo tem que ser obrigatoriamente 5
                            print("|", a1+a2+a3+a4)
                            nmrs.append(a1+a2+a3+a4)
    print(":",len(nmrs))
    



if __name__ == "__main__":
    main()