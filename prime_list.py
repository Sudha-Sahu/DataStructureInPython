

def prime_list(n1, n2):
    prime_lst = []
    for i in range(n1, n2):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
        if count == 0 and i != 1:
            prime_lst.append(i)
    return prime_lst


if __name__ == "__main__":
    array = []
    limit1 = 1
    limit2 = 100
    while limit2 < 1000:
        result = prime_list(limit1, limit2)
        array.append(result)
        limit1 += 100
        limit2 += 100

    print(array)
