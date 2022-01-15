for i in range(-1, -1*len(a := list(input())), -1):
    if a[i] > a[i-1]: a[i], a[i-1] = a[i-1], a[i]; break
print(''.join(a))
