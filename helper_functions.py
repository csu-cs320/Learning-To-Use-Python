def gcd(x, y):
    x, y = sorted([x, y])
    while True:
        r = y % x
        if r == 0: return x
        x, y = r, x

def main(x, y):
    print("The GCD of {} and {} is {}!".format(x, y, gcd(x, y)))


if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    x, y = [int(sys.argv[1]), int(sys.argv[1])] if argc >= 3 else (252, 105)
    main(x, y)
