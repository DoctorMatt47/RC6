from Round import *


def encrypt(value, main_key, r):
    K = main_key_generation(main_key, r)
    values = key_parse(value)

    values = enc_start_xor(values, K[0], K[1])

    for i in range(1, r + 1):
        values = [int(j) for j in values]
        values = enc_round(values, K[2 * i], K[2 * i + 1])

    values = enc_end_xor(values, K[2 * (r + 1)], K[2 * (r + 1) + 1])

    return values_to_string(values)


def values_to_string(values):
    values = [hex(i)[2:] for i in values]
    for i in range(len(values)):
        values[i] = "".join(["0" for t in range(8 - len(values[i]))]) + values[i]
    values = values[0] + values[1] + values[2] + values[3]
    return values.upper()


def decrypt(value, main_key, r):
    K = main_key_generation(main_key, r)
    value_mas = key_parse(value)

    value_mas = dec_start_xor(value_mas, K[2 * (r + 1)], K[2 * (r + 1) + 1])
    for i in reversed(range(1, r + 1)):
        value_mas = [int(j) for j in value_mas]
        value_mas = dec_round(value_mas, K[2 * i], K[2 * i + 1])
    value_mas = dec_end_xor(value_mas, K[0], K[1])

    return values_to_string(value_mas)


def enc_start_xor(values, K1, K2):
    A, B, C, D = values[0], values[1], values[2], values[3]
    B = mod(B + K1, 2 ** 32)
    D = mod(D + K2, 2 ** 32)
    return A, B, C, D


def enc_end_xor(values, K1, K2):
    A, B, C, D = values[0], values[1], values[2], values[3]
    A = mod(A + K1, 2 ** 32)
    C = mod(C + K2, 2 ** 32)
    return A, B, C, D


def dec_start_xor(values, K1, K2):
    A, B, C, D = values[0], values[1], values[2], values[3]
    A = mod(A - K1, 2 ** 32)
    C = mod(C - K2, 2 ** 32)
    return A, B, C, D


def dec_end_xor(values, K1, K2):
    A, B, C, D = values[0], values[1], values[2], values[3]
    B = mod(B - K1, 2 ** 32)
    D = mod(D - K2, 2 ** 32)
    return A, B, C, D
