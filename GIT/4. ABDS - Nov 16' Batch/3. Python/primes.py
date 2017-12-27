
for i in range(2, 100):
    check = 0
    for j in range(2, (i-1)):
        if i%j == 0:
            check = 1
            break
    if check == 0:
        print i, 