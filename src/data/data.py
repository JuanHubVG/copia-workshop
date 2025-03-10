import math
class Data:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        for elemento in lista:
            if elemento not in resultado:
                resultado.append(elemento)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i, j = 0, 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado

    def rotar_lista(self, lista, k):
        k %= len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_actual = sum(lista)
        return suma_esperada - suma_actual
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True

    def implementar_pila(self):
        pila = []
        return {
            'empujar': lambda x: pila.append(x),
            'pop': lambda: pila.pop() if pila else None,
            'peek': lambda: pila[-1] if pila else None,
            'igual': lambda: len(pila) == 0
        }

    def implementar_cola(self):
        cola = []
        return {
            'encolar': lambda x: cola.append(x),
            'dequeue': lambda: cola.pop(0) if cola else None,
            'peek': lambda: cola[0] if cola else None,
            'is_empty': lambda: len(cola) == 0
        }

    def matriz_transpuesta(self, matriz):
        filas, columnas = len(matriz), len(matriz[0])
        return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
