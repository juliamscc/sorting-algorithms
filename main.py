from bubble_sort import *
from insertion_sort import *
from straight_selection import *
import time, random

def crateRandomArray(size, min = 0, max = 1000, ):
    array = [random.randrange(min, max+1, 1) for i in range(size)]
    return array

def createNonSortedArray(size):
    array = []
    for i in range(1, size+1):
        array.append(i)
    return print(array)


auxTeste = 3

if(False):
    print("Bubble Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        print(lista)
        inicio = time.perf_counter_ns()
        lista = bubbleSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print(lista)
        print(f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Insertion Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        print(lista)
        inicio = time.perf_counter_ns()
        lista = insertionSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print(lista)
        print(f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Straight Selection")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        print(lista)
        inicio = time.perf_counter_ns()
        lista = straightSelection(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        print(lista)
        print(f'n = {n} Tempo de execução: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execução: {tempo/1000000000} em segundos')
        print()