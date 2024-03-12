BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE16 = "0123456789ABCDEF"

def encode(num, alphabet=BASE62):
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        print(f"num {num}, rem {rem}")
        arr.append(alphabet[rem])
    arr.reverse()
    print(f"arr {arr}")
    return ''.join(arr)

print(encode("11157"))
print(encode(42, alphabet=BASE16))