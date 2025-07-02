



def find_matching_parantesys(s,index):
    stack = 1
    i = index
    if s[i] == "[":

        while stack !=0:
            i += 1
            if s[i] == "[":
                stack += 1
            elif s[i] == "]":
                stack -= 1


    elif s[i] == "]":

        while stack !=0:
            i -= 1
            if s[i] == "]":
                stack += 1
            elif s[i] == "[":
                stack -= 1

    else:
        raise IndexError("You have no \"[\" or \"]\" at the index")

    return i








class BF_interpreter():

    def __init__(self):
        self.instruction_pointer = 0

        self.data_pointer = 0

        self.byte_array = [0] * 300000

    def output(self):
        print(bytes(self.byte_array).decode('ascii')[self.data_pointer], end="")

    def input(self):
        self.byte_array[self.data_pointer] = ord(input())

    def run_code(self, code):
        print("Running...")
        print()

        try:
            while self.instruction_pointer < len(code):  # this loop is the meat of the interpreter
                    #print(f"Instruction pointer is at:{self.instruction_pointer} with instruction: {code[self.instruction_pointer]}")
                    #print(f"Data pointer is at:{self.data_pointer} with data: {self.byte_array[self.data_pointer]}")

                    if code[self.instruction_pointer] == '>':
                        self.data_pointer += 1
                    elif code[self.instruction_pointer] == '<':
                        self.data_pointer -= 1
                        if self.data_pointer < 0:
                            raise IndexError("Negative pointer!")
                    elif code[self.instruction_pointer] == '+':
                        self.byte_array[self.data_pointer] += 1
                        if self.byte_array[self.data_pointer] > 127:
                            self.byte_array[self.data_pointer] = 0
                    elif code[self.instruction_pointer] == '-':
                        self.byte_array[self.data_pointer] -= 1

                        if self.byte_array[self.data_pointer] < 0:
                            self.byte_array[self.data_pointer] = 127

                    elif code[self.instruction_pointer] == '.':
                        self.output()
                    elif code[self.instruction_pointer] == ',':
                        self.input()

                    elif code[self.instruction_pointer] == '[' and self.byte_array[self.data_pointer] == 0:
                       self.instruction_pointer = find_matching_parantesys(code,self.instruction_pointer)
                    elif code[self.instruction_pointer] == ']' and self.byte_array[self.data_pointer] != 0:
                        self.instruction_pointer = find_matching_parantesys(code,self.instruction_pointer)


                    self.instruction_pointer += 1
            print()

        except Exception as err:
            print(f"ERROR:{err}")

        else:
            print(f"Code executed succesfully! (instruction pointer {self.instruction_pointer} == code length {len(code)}) ")

        input("Press Enter to continue...")




def main():
    print(find_matching_parantesys("[[[.]..]]",8))


if __name__ == "__main__":
    main()

