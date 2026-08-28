# Funzione Forza Peso

def forza(massa):

    return massa * 9.81
    
print("---Forza Peso---\n")

# Inserimento massa

massa = float(input("Inserisci la massa(in Kg): "))

# Chiamata funzione Forza peso

peso = forza(massa)

# Risultato

print(("Forza Peso: ") + str(peso) + (" N/Kg"))
