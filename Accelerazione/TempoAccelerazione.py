# Funzione tempo

def tempo(velocita,accelerazione):

    return velocita/accelerazione

print("---Tempo---\n")

# Inserimento velocità

velocita = float(input("Inserisci velocità: "))

# Inserimento accelerazione

accelerazione = float(input("Inserisci accelerazione: "))

# Chimata funzione tempo e risultato

risultato = tempo(velocita,accelerazione)
print(("Tempo: ") + str(risultato) + (" s"))
