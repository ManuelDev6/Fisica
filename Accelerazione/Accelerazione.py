# Funzione accelerazione

def accelerazione(velocita,tempo):

    return velocita / tempo

print("---Accelerazione---\n")

# Inserimento velocità

velocita = float(input("Inserisci velocità: "))

# Inserimento spazio

spazio = float(input("Inserisci spazio: "))

# Chiamata funzione accelerazione e risultato

risultato = accelerazione(velocita,spazio)
print(("Accelerazione: ") + str(risultato) + (" m/s2"))
