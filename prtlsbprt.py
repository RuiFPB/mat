"""
Calcula de quantos modos diferentes é possivel fazer o trajeto Porto-Lisboa-Porto, usando transportes diferentes para a ida e para a volta
"""

def main():
    transportes = ["comboio ", "automóvel ", "avião "]
    possibilidades = []


    for ti in transportes:
        for tv in transportes:
            if tv != ti:
                print(ti+tv)
                possibilidades.append(ti+tv)

    print(len(possibilidades))


if __name__ == "__main__":
    main()