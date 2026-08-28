# Funzione spazio

def spazio(velocita,tempo):

    return velocita * tempo

print("---Spazio---")

# Inserimento velocità

velocita = float(input("\nInserisci velocità: "))

# Inserimento tempo

tempo = float(input("Inserisci tempo: "))

# Chiamata funzione spazio e risultato

risultato = spazio(velocita,tempo)
print(("Risultato: ") + str(risultato) + (" m"))
