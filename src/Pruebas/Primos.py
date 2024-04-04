for i in range (50, 101):
    j = 2
    cond = True
    while True:
        if i % j == 0 and i != j:
            print(f"{i} no es numero primo")
            break
        elif i % j != 0:
            j += 1
            continue
        else:
            print(f"{i} es numero primo")
            break
        