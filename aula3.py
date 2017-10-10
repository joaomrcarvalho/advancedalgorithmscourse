import random


def brute_force(lista):
    count = 0
    for i in lista:
        if i % 2 == 0:
            count += 1
    return count


def decrease_and_conquer(lista):
    is_even = (lista[0] % 2 == 0)

    if len(lista) == 1:
        return is_even

    elif len(lista) > 1:
        return is_even + decrease_and_conquer(lista[1:])


def divide_and_conquer(lista):
    if len(lista) == 1:
        return lista[0] % 2 == 0

    middle = len(lista) // 2

    return divide_and_conquer(lista[:middle]) + divide_and_conquer(lista[middle:])


def search_iterative(lista, num):
    for index in range(len(lista)):
        if lista[index] == num:
            return index
    return -1


def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    if n == 0 or n == 1:
        return n

    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[i-2] + fibs[i-1])
    return fibs[n-1]


def binomial_recursive(n, j):
    if j == 0 or j == n:
        return 1

    return binomial_recursive(n-1, j) + binomial_recursive(n-1, j-1)


# TODO
def binomial_dynamic(n):
    lista = []
    for j in range(n):
        lista.append(1)


def main():
    # numero = 10
    # lista = random.sample(range(20), 10)
    # print(lista)
    # print("numero de pares: ", decrease_and_conquer(lista))
    # index = search_iterative(lista, numero)
    # if index != -1:
    #     print("à procura do número ", numero, "encontrado no index ", index)
    # else:
    #     print("numero não encontrado!")

    # # TEST fibonacci
    # for i in range(20):
    #     print(fibonacci_iterative(i))

    print(binomial_recursive(7, 3))


if __name__ == "__main__":
    main()
