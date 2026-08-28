# Funzione tempo

def tempo(spazio,velocita):

    return spazio / velocita

print("---Tempo---")

# Inserimento spazio

spazio = float(input("\nInserisci spazio: "))

# Inserimento velocità

velocita = float(input("Inserisci velocità: "))

# Chiamata funzione tempo e risultato

risultato = tempo(spazio,velocita)
print(("Tempo: ") + str(risultato) + (" s"))
