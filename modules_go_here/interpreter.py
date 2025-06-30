
import sys













def runner(program):
    instruction_pointer = 0

    data_pointer = 0

    byte_array = [0] * 30000  # an array of bytes from 0 to 255 of 30,000 elements

    def BF_output():

        print(bytes(byte_array).decode('ascii')[data_pointer], end="")

    def BF_input():
        byte_array[data_pointer] = ord(input())

    while instruction_pointer < len(program): #this loop is the meat of the interpreter
        # print(f"Instruction pointer is at:{instruction_pointer} with instruction: {program[instruction_pointer]}")
        # print(f"Data pointer is at:{data_pointer} with data: {byte_array[data_pointer]}")
        try:
            if program[instruction_pointer] == '>':
                data_pointer += 1
            elif program[instruction_pointer] == '<':
                data_pointer -= 1
            elif program[instruction_pointer] == '+':
                byte_array[data_pointer] += 1
            elif program[instruction_pointer] == '-':
                byte_array[data_pointer] -=1
            elif program[instruction_pointer] == '.':
                BF_output()
            elif program[instruction_pointer] == ',':
                BF_input()

            elif program[instruction_pointer] == '[':
                if byte_array[data_pointer] == 0:
                    while program[instruction_pointer] != ']':
                        instruction_pointer += 1
            elif program[instruction_pointer] == ']':
                if byte_array[data_pointer] != 0:
                    while program[instruction_pointer] != '[':
                        instruction_pointer -= 1
            else:
                pass

        except IndexError:
            print(f"Error the current address you are trying to access is {instruction_pointer} with a maximum of {len(program)}")
            break

        finally:
            instruction_pointer += 1






def main():
    program = input("Enter your program:")

    print("Running...")

    runner(program)



    print("\nProgram execution complete!")

if __name__ == "__main__":
    main()