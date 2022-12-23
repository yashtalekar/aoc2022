

def find_common_letter(s):
    halfLength = int((len(s) - 1)/2)
    # print(halfLength)

    firstHalf = s[:halfLength]
    secondHalf = s[halfLength:]
    # print(firstHalf)
    for letter in firstHalf:
        if letter in secondHalf:
            return letter
    return "Error"


def convert_char_to_val(s):
    if s.isupper():
        baseVal = 27
        Val = baseVal + ord(s) - ord("A")
        return Val
    else:
        baseVal = 1
        Val = baseVal + ord(s) - ord("a")
        return Val


with open("3a.input", "r")  as f:

    lines = f.readlines()
    # test = find_common_letter(lines[0])
    # print(convert_char_to_val(test))

    sum = 0
    for line in lines:
        if line == "\n":
            break
        sum += convert_char_to_val(find_common_letter(line))

    print(sum)
