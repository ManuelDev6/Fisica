# Funzione forza elastica

def forza(a,b):

    return a * b

print("---Forza Elastica---\n")

# Inserimento costante elastica

costante = float(input("Inserisci la costante elastica: "))

# Inserimento spostamento molla

spostamento = float(input("Inserisci lo spostamento della molla: "))

# Chiamata funzione forza elastica e risultato

risultato = forza(costante,spostamento)
print(("\nForza elastica: ") + str(risultato) + (" N/m"))
