from wrapping import memo


NADDS = 0


# dellanoy_numbers
def D_recursive(m, n):
    if m == 0 or n == 0:
        return 1
    global NADDS
    NADDS += 2
    return D_recursive(m-1, n) + D_recursive(m-1, n-1) + D_recursive(m, n-1)


D_recursive = memo(D_recursive)


# row coin problem
def row_coin_recursive(n, coins):
    if n == 0:
        return 0
    if n == 1:
        return coins[1]

    return max(coins[n] + row_coin_recursive(n-2, coins), row_coin_recursive(n-1, coins))


def main_1():
    global NADDS
    for m in range(10):
        for n in range(10):
            NADDS = 0
            print("D_recursive(", m,",", n, "=", D_recursive(m, n), ")")
            print("NADDS", NADDS)
        print("------")


def main_2():
    coins = [None, 5, 1, 2, 10, 6, 2]
    print(row_coin_recursive(n=len(coins)-1, coins=coins))


if __name__ == "__main__":
    main_1()
    # main_2()


