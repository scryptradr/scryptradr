import math as m


def sigmoid(x):
    return 1 / (1 + pow(m.e, -0.2 * x))


def sigmoid_reverse(x):
    return -5 * m.log((1 / x) - 1, m.e)
