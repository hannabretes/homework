for i in range(6):
    print()
    for j in range(8):
        if j % 2 == i % 2:
            print("#", end=" ")
        else:
            print(" ", end="")
print()