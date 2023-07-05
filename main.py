from bubble_sort import *
from insertion_sort import *
from straight_selection import *
from quick_sort import *
from merge_sort import *
from shell_sort import *
from heap_sort import *
import time, random

def crateRandomArray(size, min = 0, max = 1000, ):
    random.seed(1)
    array = [random.randrange(min, max+1, 1) for i in range(size)]
    return array

def createNonSortedArray(size):
    array = []
    for i in range(1, size+1):
        array.append(i)
    return print(array)


# Testes dos algoritmos de ordenação
auxTeste = 6

if(False):
    print("Bubble Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        # print(lista)
        inicio = time.perf_counter_ns()
        lista = bubbleSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        # print(lista)
        print(f'n = {n} Tempo de execucao: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Insertion Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        # print(lista)
        inicio = time.perf_counter_ns()
        lista = insertionSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        # print(lista)
        print(f'n = {n} Tempo de execucao: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Straight Selection")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        # print(lista)
        inicio = time.perf_counter_ns()
        lista = straightSelection(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        # print(lista)
        print(f'n = {n} Tempo de execucao: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Quick Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        # print(lista)
        inicio = time.perf_counter_ns()
        lista = quickSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        # print(lista)
        print(f'n = {n} Tempo de execucao: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Merge Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        # print(lista)
        inicio = time.perf_counter_ns()
        lista = mergeSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        # print(lista)
        print(f'n = {n} Tempo de execucao: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Shell Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        # print(lista)
        inicio = time.perf_counter_ns()
        lista = shellSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        # print(lista)
        print(f'n = {n} Tempo de execucao: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000000} em segundos')
        print()

if(False):
    print("Heap Sort")
    n = 1
    for i in range(1, auxTeste):
        n = n*10
        lista = crateRandomArray(n)
        # print(lista)
        inicio = time.perf_counter_ns()
        lista = heapSort(lista)
        fim = time.perf_counter_ns()
        tempo = (fim - inicio)
        # print(lista)
        print(f'n = {n} Tempo de execucao: {tempo} nanossegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000} em microssegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000} em milissegundos')
        print(f'n = {n} Tempo de execucao: {tempo/1000000000} em segundos')
        print()