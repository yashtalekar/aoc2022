with open("1a.input", "r") as f:
    lines = f.readlines()

    sums = []
    currentTotal = 0
    for i in range(len(lines)):
        if lines[i] != "\n":
            val = int(lines[i])
            currentTotal += val
            if (i == len(lines) - 1):
                sums.append(currentTotal)

        else:
            sums.append(currentTotal)
            currentTotal = 0

    sums.sort(reverse=True)
    print(sums[0] + sums[1] + sums[2])
