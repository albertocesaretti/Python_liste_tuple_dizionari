# Lista di numeri interi
numeri = [11, 22, 33, 44, 55]

# Lista di stringhe
nomi = ["Alice", "Bob", "Charlie"]

# Lista mista di diversi tipi di dati
mista = [1, "ciao", 3.14, True]

# Lista vuota
vuota = []

print("***** prima modalità *****")
print(len(nomi))
for i in range(len(nomi)):
    print("stampo indice e valore :", i, nomi[i])

print("***** seconda modalità *****")
i = 0
for numero in numeri:
    print("stampo indice e valore : ", i, numero)
    i +=1
    
print("******* terza modalità ******")
for indice,valore in enumerate(mista):
    print("stampo indice e valore : ", indice, valore)
    
# Lista di numeri interi
numeri = [6, 9, 7, 4, 5]

# Lista di stringhe
nomi = ["Alice", "Bob", "Charlie", "Alice"]

# Lista mista di diversi tipi di dati
mista = [1, "ciao", 3.14, True]

# Lista vuota
vuota = []

print("**** metodi delle liste ***")
print("*** append() alla fine lista***")
vuota.append("cane")
vuota.append("gatto")
print(vuota)
print("*** insert(indice,elemento) in posizione precisa***")
vuota.insert(1,"criceto")
print(vuota)
print("***** remove(elemento) rimuove elemento******")
vuota.remove("cane")
print(vuota)
print("***** pop(indice) rimuove elemento******")
vuota.pop(1)
print(vuota)
print("***** sort() ordina gli elementi******")
numeri.sort()
print(numeri)
print("***** reverse() inverte gli elementi******")
numeri.reverse()
print(numeri)
print("***** clear() rimuove gli elementi******")
vuota.clear()
print(vuota)
print("***** copy() copia la lista******")
nomi_2 = nomi.copy()
print(nomi_2)
print("****** count(elemento) numero di volte che compare un elemento***")
n = nomi.count("Alice")
print(n)
print("***** index(elemento) ******")
i = nomi.index("Bob")
print("indice risulta",i)









    

