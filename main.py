from Enc_Dec import encrypt, decrypt


def main():
    data = "1DAA113E8E5BE4F0050AA8ECC1D8BF14"
    key = "85BE53ECE50ABA11C3F3AAFD5CFA6CB4"
    round = 20

    print("data: ", data)
    print("key: ", key)
    print("round: ", round)

    encrypted = encrypt(data, key, round)
    print("encrypted: ", encrypted)

    decrypted = decrypt(encrypted, key, round)
    print("decrypted: ", decrypted)

    assert (decrypted == data)


if __name__ == '__main__':
    main()
