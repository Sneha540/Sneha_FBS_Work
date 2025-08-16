for i in range(1,6):
    for j in range(1, 7- i):
        if j == 1 or i == 1 or i+j==6:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()


