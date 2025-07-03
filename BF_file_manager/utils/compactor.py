




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


def code_expander(data):#not finished
    code = ""
    data =bin(data)[2:]
    for _ in range(3-len(data)//3):
        data = "0" + data
    while data != "":
        print(data)
        instruction = data[len(data)-3:]
        if instruction == "000":
            code = code + ">"
        elif instruction == "001":
            code = code + "<"
        elif instruction == "010":
            code = code + "+"
        elif instruction == "011":
            code = code + "-"
        elif instruction == "100":
            code = code + "."
        elif instruction == "101":
            code = code + ","
        elif instruction == "110":
            code = code + "["
        elif instruction == "111":
            code = code + "]"
        data = data[:len(data)-3]
    return code

def main():

    data = code_compactor("<,<.")
    print(bin(data))
    print(code_expander(data))


if __name__ == "__main__":
    main()