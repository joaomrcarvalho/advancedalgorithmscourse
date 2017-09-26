NMULTS=0


def A(a, b):
    global NMULTS
    res = 1
    for i in range(b):
        res *= a
        NMULTS += 1
    return res


def B(a, b):
    global NMULTS
    if b == 0:
        return 1

    NMULTS += 1
    return a * B(a, b-1)


def C(a, b):
    global NMULTS
    if b == 0:
        return 1
    if b == 1:
        return a

    NMULTS += 1
    return C(a, b//2) * C(a, (b+1)//2)


def D(a, b):
    global NMULTS
    if b == 0:
        return 1

    # even
    if b % 2 == 0:
        NMULTS += 1
        return D(a, b//2)**2
    # odd
    else:
        NMULTS+=2
        return a * D(a, b//2)**2


def main():
    global NMULTS
    a = 2
    for i in range(0, 21):
        NMULTS = 0
        res = D(a, i)
        print("(%3d^%3d) = %10d        NMULTS = %10d" % (a, i, res, NMULTS))


if __name__ == "__main__":
    main()
