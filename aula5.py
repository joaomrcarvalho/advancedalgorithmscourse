import random
from collections import Counter


# COIN
def toss_coin(tails_prob=0.5):
    if random.random() < tails_prob:
        return "tails"

    return "heads"


def toss_coin_n_times(n):
    return [toss_coin(0.5) for _ in range(n)]


print("--------------")
print("COIN EXPERIMENT:")
a = Counter(toss_coin_n_times(1000))
print(dict(a))
print("--------------")


# DICE
def toss_dice(n, probs=None):
    if probs is None:
        probs = [1/n for _ in range(n)]

    cum_sums = [sum(probs[0:i+1]) for i in range(len(probs))]
    rand = random.random()
    return next(cum_sums.index(obj)+1 for obj in cum_sums if rand < obj)


def toss_dice_k_times(k):
    return [toss_dice(n=6) for _ in range(k)]


print("DICE EXPERIMENT:")
b = Counter(toss_dice_k_times(1000))
print(dict(b))
print("--------------")


# DICE-COIN EXPERIMENT
def toss_dice_coin():
    number_of_coin_tosses = toss_dice(n=6)
    # print("Dice:", number_of_coin_tosses)
    return dict(Counter(toss_coin_n_times(number_of_coin_tosses)))


def toss_dice_coin_k_times(k):
    tmp = [toss_dice_coin() for _ in range(k)]
    return tmp


print("DICE COIN EXPERIMENT:")
print(toss_dice_coin_k_times(1000))

