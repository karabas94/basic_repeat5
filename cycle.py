height = int(input("Enter half of diagonal length for square: "))

print("A")
for h in range(height):
    for i in range(h):
        print(" ", end=" ")
    for j in range(h, height):
        print("*", end=" ")
    for w in range(h, height-1):
        print("*", end=" ")
    for k in range(h):
        print("*", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print(" ", end=" ")
    for j in range(h+1):
        print(" ", end=" ")
    for w in range(h):
        print(" ", end=" ")
    for k in range(h, height-1):
        print("*", end=" ")
    print()

print("Б")
for h in range(height):
    for i in range(h):
        print("*", end=" ")
    for j in range(h, height):
        print(" ", end=" ")
    for w in range(h, height-1):
        print(" ", end=" ")
    for k in range(h):
        print(" ", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print("*", end=" ")
    for j in range(h+1):
        print("*", end=" ")
    for w in range(h):
        print("*", end=" ")
    for k in range(h, height-1):
        print(" ", end=" ")
    print()

print("В")
for h in range(height):
    for i in range(h):
        print(" ", end=" ")
    for j in range(h, height):
        print("*", end=" ")
    for w in range(h, height-1):
        print("*", end=" ")
    for k in range(h):
        print(" ", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print(" ", end=" ")
    for j in range(h+1):
        print(" ", end=" ")
    for w in range(h):
        print(" ", end=" ")
    for k in range(h, height-1):
        print(" ", end=" ")
    print()

print("Г")
for h in range(height):
    for i in range(h):
        print(" ", end=" ")
    for j in range(h, height):
        print(" ", end=" ")
    for w in range(h, height-1):
        print(" ", end=" ")
    for k in range(h):
        print(" ", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print(" ", end=" ")
    for j in range(h+1):
        print("*", end=" ")
    for w in range(h):
        print("*", end=" ")
    for k in range(h, height-1):
        print(" ", end=" ")
    print()

print("Д")
for h in range(height-1):
    for i in range(h):
        print(" ", end=" ")
    for j in range(h, height):
        print("*", end=" ")
    for w in range(h, height-1):
        print("*", end=" ")
    for k in range(h):
        print(" ", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print(" ", end=" ")
    for j in range(h+1):
        print("*", end=" ")
    for w in range(h):
        print("*", end=" ")
    for k in range(h, height-1):
        print(" ", end=" ")
    print()

print("Е")
for h in range(height + 1):
    for i in range(h):
        print("*", end=" ")
    for j in range(h, height):
        print(" ", end=" ")
    for w in range(h, height - 1):
        print(" ", end=" ")
    for k in range(h):
        if k == height-1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
for h in range(height):
    for i in range(h, height - 1):
        print("*", end=" ")
    for j in range(h + 1):
        print(" ", end=" ")
    for w in range(h):
        print(" ", end=" ")
    for k in range(h, height - 1):
        print("*", end=" ")
    print()

print("Ж")
for h in range(height+1):
    for i in range(h):
        print("*", end=" ")
    for j in range(h, height):
        print(" ", end=" ")
    for w in range(h, height-1):
        print(" ", end=" ")
    for k in range(h):
        print(" ", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print("*", end=" ")
    for j in range(h+1):
        print(" ", end=" ")
    for w in range(h):
        print(" ", end=" ")
    for k in range(h, height-1):
        print(" ", end=" ")
    print()

print("З")
for h in range(height):
    for i in range(h):
        print(" ", end=" ")
    for j in range(h, height-1):
        print(" ", end=" ")
    for w in range(h, height-1):
        print(" ", end=" ")
    for k in range(h+1):
        print("*", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print(" ", end=" ")
    for j in range(h+1):
        print(" ", end=" ")
    for w in range(h):
        print(" ", end=" ")
    for k in range(h, height-1):
        print("*", end=" ")
    print()

print("И")
for h in range(height):
    for i in range(h):
        print("*", end=" ")
    for j in range(h, height):
        print("*", end=" ")
    for w in range(h, height-1):
        print("*", end=" ")
    for k in range(h):
        print("", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print("*", end=" ")
    for j in range(h+1):
        print(" ", end=" ")
    for w in range(h):
        print(" ", end=" ")
    for k in range(h, height-1):
        print(" ", end=" ")
    print()

print("К")
for h in range(height):
    for i in range(h):
        print(" ", end=" ")
    for j in range(h, height):
        print(" ", end=" ")
    for w in range(h, height-1):
        print(" ", end=" ")
    for k in range(h):
        print("*", end=" ")
    print()
for h in range(height):
    for i in range(h, height-1):
        print(" ", end=" ")
    for j in range(h+1):
        print("*", end=" ")
    for w in range(h):
        print("*", end=" ")
    for k in range(h, height-1):
        print("*", end=" ")
    print()