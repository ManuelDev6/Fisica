# Funzione velocità

def velocita(spazio,tempo):

    return spazio / tempo

print("---Velocità---")

# Inserimento spazio

spazio = float(input("\nInserisci spazio: "))

# Inserimento tempo

tempo = float(input("Inserisci tempo: "))

# Chimata funzione velocità e risultato

risultato = velocita(spazio,tempo)
print(("\nVelocità: ") + str(risultato) + (" m/s"))
