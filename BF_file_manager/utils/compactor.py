




def code_compactor(code):
    data = 0b000
    for char in code:

        if char == '>':
            data = data | 0
        elif char == '<':
            data = data | 1
        elif char == '+':
            data = data | 2
        elif char == '-':
            data = data | 3
        elif char == '.':
            data = data | 4
        elif char == ',':
            data = data | 5
        elif char == '[':
            data = data | 6
        elif char == ']':
            data = data | 7
        else:
            raise ValueError("Invalid data input to the compactor")

        data = data << 3

    data = data >> 3
    return data


def code_expander(data):
    code = ""

    while data > 0:
        instruction = data

def main():

    data = bin(code_compactor("<<"))
    print("This be end result:",data)
    print(data[2:])
    print(len(data[2:])//3)


if __name__ == "__main__":
    main()