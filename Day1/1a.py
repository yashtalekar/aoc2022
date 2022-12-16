

# f = open("1a.input", "r")

with open("1a.input", "r") as f:
    lines = f.readlines()
    max = 0

    currentTotal = 0
    for i in range(len(lines)):
        if lines[i] != "\n":
            val = int(lines[i])
            currentTotal += val

        else:
            if currentTotal >= max:
                max = currentTotal
            currentTotal = 0

    print(max)