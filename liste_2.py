#lista animali
animali = ["cane", "gatto","criceto","pesce rosso", "pappagallo"]

# Lista di numeri interi
numeri = [6, 4, 7, 2, 5]

# Lista di stringhe
nomi = ["Alice", "Bob", "Charlie"]

# Lista mista di diversi tipi di dati
mista = [1, "ciao", 3.14, True]

# Lista vuota
vuota = []

print(animali[0])
print(animali[-1])

animali[4] = "topolino"
print(animali)
#slicing
print(nomi[0:2])

#append() inserisce un elemento in ultima posizione
print(vuota)
vuota.append("Mario")
vuota.append("Alice")
vuota.append("Alberto")
vuota.append("Luigi")
print(vuota)
#pop() rimuove un elemento in ultima posizione
vuota.pop()
print(vuota)
#insert() aggiunge un elemento in una posizione specifica
vuota.insert(1,"Roberto")
print(vuota)
#remove() rimuove un elemento specificato
vuota.remove("Alberto")
print(vuota)
#sort() ordina gli elememti
numeri.sort()
print(numeri)
#reverse()
numeri.reverse()
print(numeri)
#clear() rimuove gli elementi
vuota.clear()
print(vuota)
#Tre modalità per scorrere le liste

for i in range(len(animali)):
    print("indice e valore con range", i, animali[i])

i = 0
for elemento in animali:
    print("indice e valore",i, elemento)
    i +=1
    
for indice, valore in enumerate(animali):
    print(indice, valore)



