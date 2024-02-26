#!/usr/bin/env python3
""" Ordena la lista principal según el segundo elemento de la listas que contiene """

def ordena_listas(lista):
    return lista[1]

x = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
print("Ordena la lista principal según el segundo elemento de la listas que contiene ")
print(x)
x.sort(key=ordena_listas)
print("\nLista ordenada:")
print(x)
