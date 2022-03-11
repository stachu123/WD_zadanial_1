import math
# Zadanie 1
lista_sportow = ["tenis", "piłka nożna", "kolarstwo", "siatkówka"]
#print(lista_sportow)
lista_sportow.reverse()
#print(lista_sportow)
lista_sportow.append("koszykówka")
lista_sportow.append("hokej")
lista_sportow.append("skoki narciarskie")

#Zadanie 2
skróty = {
    "np": "Na Przykład",
    "itp": "i tym podobne",
    "etc": "et cetera",
    "itd": "i tak dalej",
}

#zadanie 3
gry = {
    "Wiedzmin 3" : "RPG",
    "Euro truck simulator 2": "Symulator",
    "Metin 2": "MMORPG",
    "Counter Strike": "strzelanka pierwszosobowa"
}

#print(len(gry))

#zadanie 4
# slowo = input("napisz jakieś zdanie")
# count = 0
# for i in slowo:
#     if i == "a":
#         count += 1
# print(count)

#zadanie 5
# pierwsza = int(input("podaj pierwsza liczbe: "))
# druga = int(input("druga liczbe: "))
# trzecia = int(input("trzecia liczbe"))
#
# wynik = pierwsza ** druga + trzecia
# f = open("liczby.txt", "w")
# f.write(f"wynik dzialania to {wynik}")
# f.close()
# f = open("liczby.txt", "r")
# print(f.readline())

# zadanie 6
# lista =[]
#
# for i in range(3):
#     a = int(input("podaj liczbe do posortowania"))
#     lista.append(a)
#
# if lista[0] > lista[1] and lista[0] > lista[2]:
#     if lista[1] > lista[2]:
#          print(f"posortowane liczby: {lista[0]} {lista[1]} {lista[2]}")
#     else:
#          print(f"posortowane liczby: {lista[0]} {lista[2]} {lista[1]}")
# if lista[1] > lista[0] and lista[1] > lista[2]:
#     if lista[2] > lista[0] and lista[1] > lista[0]:
#          print(f"posortowane liczby: {lista[1]} {lista[2]} {lista[0]}")
#     else:
#          print(f"posortowane liczby: {lista[1]} {lista[0]} {lista[2]}")
#
# if lista[2] > lista[0] and lista[2] > lista[1]:
#     if lista[1] > lista[0] and lista[1] > lista[0]:
#         print(f"posortowane liczby: {lista[2]} {lista[1]} {lista[0]}")
#     else:
#         print(f"posortowane liczby: {lista[2]} {lista[0]} {lista[1]}")

# #zadanie 7
#
# lista = [2, 5, 5.12, 6.21]
# new_list = []
# for i in lista:
#     i = i**2
#     new_list.append(i)
#
# print(new_list)

# # zadanie 8
# parzyste = []
# count = 0
# while count != 10:
#     i = int(input("podaj liczbe"))
#     if i % 2 == 0:
#         parzyste.append(i)
#         count += 1
#     else:
#         count += 1
#
# print(parzyste)

#zadanie 9

liczba = int(input("podaj liczbe"))

if liczba > 0:
    liczba = math.sqrt(liczba)
    print(liczba)
else:
    print("liczba nie moze byc ujemna")
