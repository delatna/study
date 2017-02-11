def dec_to_bin(a):
    if a // 2:
        print(a%2)
    else:
        return dec_to_bin(a//2)

dec_to_bin(12)
