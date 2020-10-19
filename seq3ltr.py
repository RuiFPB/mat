'''
Gera uma sequencia de três letras, começando por uma vogal e terminando numa consoante.
'''


def main():
    letras = "abcdefghijklmnopqrstuvwxyz"
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    seq = []

    for l1 in vogais:
        #print("|>>", l1)
        for l2 in letras:
            if l2 != l1:
                #print("|>", l1+l2)
                for l3 in consoantes:
                    if l3 != l2:
                        print("|",l1+l2+l3)
                        seq.append((l1+l2+l3))
    
    print(len(seq))



if __name__ == "__main__":
    main()