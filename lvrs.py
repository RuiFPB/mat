"""
Determina quantas combinações de 2 livros diferentes são possiveis apartir de 5 romances, 2 bd, 3 aventura.
"""

def main():
    livros = "rrrrrbbaaa"
    poss = []
    for l1 in livros:
        for l2 in livros:
            if l2 != l1:
                if l2+l1 not in poss: # a combinação bd-avent é semelhante a avent-bd neste contexto, por isso é eliminada
                    print("|", l1+l2)
                    poss.append(l1+l2)

    print(len(poss))


if __name__ == "__main__":
    main()