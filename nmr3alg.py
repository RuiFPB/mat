"""
Determina quantos numeros de 3 algarimos distintos existem
"""

def main():
    numeros = "0123456789"
    seq = []


    for n1 in numeros:
        if n1 != "0":
            for n2 in numeros:
                if n2 != n1:
                    for n3 in numeros:
                        if n3 != n1 and n3 != n2:
                            print("|"+n1+n2+n3)
                            seq.append(n1+n2+n3)

                        
    print("total:",len(seq))


if __name__ == "__main__":
    main()