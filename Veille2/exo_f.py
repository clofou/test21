# calcul du factorielle


def factorielle(n):
    if n == 1:
        factorielle_t = 1
    else:
        factorielle_t = n *  factorielle(n-1)
    return factorielle_t

numb = int(input('Entrer un nombre positif: '))
print("factorielle de {} = "+str(factorielle(numb)))
