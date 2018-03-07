def number_needed(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] not in b:
            a.replace(a[i], '', 1)
            c += 1
    for i in range(len(b)):
        if b[i] not in a:
            b.replace(b[i], '', 1)
            c += 1
    print(a)
    print(b)
    return c

a = input()
b = input()

print(number_needed(a, b))
