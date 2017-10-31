import random
from collections import Counter


# DICE
def toss_dice(n, probs=None):
    if probs is None:
        probs = [1/n for _ in range(n)]

    cum_sums = [sum(probs[0:i+1]) for i in range(len(probs))]
    rand = random.random()
    return next(cum_sums.index(obj)+1 for obj in cum_sums if rand < obj)


# implemented using exhaustive list
resultados = list()
while True:
    dado = toss_dice(4000)

    if dado in resultados:
        resultados.append(dado)
        break

    resultados.append(dado)

print("lançamentos = ", resultados)
print(len(resultados))


# implemented using "array-like" list
num_faces = 200
resultados = [0] * num_faces
num_lancamentos = 0

while True:
    dado = toss_dice(num_faces)
    num_lancamentos += 1
    if resultados[dado] == 1:
        resultados[dado] += 1
        break

    resultados[dado] += 1

print("lançamentos = ", resultados)
print(num_lancamentos)


# implemented using "array-like" list
# all elements at least 1 time
num_faces = 200
resultados = [0] * (num_faces+1)
num_lancamentos = 0

while True:
    dado = toss_dice(num_faces)
    num_lancamentos += 1
    if all(resultados[1:]):
        resultados[dado] += 1
        break

    resultados[dado] += 1

print("lançamentos = ", resultados)
print(num_lancamentos)

