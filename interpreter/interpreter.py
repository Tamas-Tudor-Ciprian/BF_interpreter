

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
        while self.instruction_pointer < len(code):  # this loop is the meat of the interpreter
            # print(f"Instruction pointer is at:{instruction_pointer} with instruction: {program[instruction_pointer]}")
            # print(f"Data pointer is at:{data_pointer} with data: {byte_array[data_pointer]}")
            try:
                if code[self.instruction_pointer] == '>':
                    self.data_pointer += 1
                elif code[self.instruction_pointer] == '<':
                    self.data_pointer -= 1
                elif code[self.instruction_pointer] == '+':
                    self.byte_array[self.data_pointer] += 1
                elif code[self.instruction_pointer] == '-':
                    self.byte_array[self.data_pointer] -= 1
                elif code[self.instruction_pointer] == '.':
                    self.output()
                elif code[self.instruction_pointer] == ',':
                    self.input()

                elif code[self.instruction_pointer] == '[':
                    if self.byte_array[self.data_pointer] == 0:
                        while code[self.instruction_pointer] != ']':
                            self.instruction_pointer += 1
                elif code[self.instruction_pointer] == ']':
                    if self.byte_array[self.data_pointer] != 0:
                        while code[self.instruction_pointer] != '[':
                            self.instruction_pointer -= 1
                else:
                    pass

            except IndexError:
                print(
                    f"Error the current address you are trying to access is {self.instruction_pointer} with a maximum of {len(code)}")
                break

            finally:
                self.instruction_pointer += 1


