from Key_generation import *


def enc_round(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    t = lcm(f(B), 5)
    u = lcm(f(D), 5)
    A = mod(lcm(A ^ t, mod(u, 32)) + K1, 2**32)
    C = mod(lcm(C ^ u, mod(t, 32)) + K2, 2**32)
    return B, C, D, A


def dec_round(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    t_1 = lcm(f(A), 5)
    t_2 = lcm(f(C), 5)
    D = rcm(mod(D - K1, 2**32), mod(t_2, 32)) ^ t_1
    B = rcm(mod(B - K2, 2**32), mod(t_1, 32)) ^ t_2
    return D, A, B, C


def f(x):
    return mod(x * (2 * x + 1), 2**32)
