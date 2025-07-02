from BF_file_manager.file_manager import *
from interpreter.interpreter import *
import sys



def main():
    file_location  = sys.argv[1]

    file = BF_file(file_location)

    base, current = os.path.splitext(file_location)

    if current == '.txt':
        file.txt_to_bf(file_location)
    else:
        interpreter = BF_interpreter()

        interpreter.run_code(file.read())

if __name__ == "__main__":
    main()