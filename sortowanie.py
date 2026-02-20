def sortowanie_przez_wstawienie(lista, n):

    for i in range(1, n):
        pom = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > pom: 
            lista[j + 1] = lista[j]
            j-=1
        lista[j+1] = pom

n = int(input("Podaj wielość zbioru: "))
lista = []
for i in range(n):
    lista.append(int(input()))
sortowanie_przez_wstawienie(lista, n)

print(* lista)