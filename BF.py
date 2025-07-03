from BF_file_manager.file_manager import *
from interpreter.interpreter import *
import sys



def main():
    interpreter = BF_interpreter()



    if len(sys.argv)>1:

        file_location  = sys.argv[1]



        file = BF_file(file_location)

        base, current = os.path.splitext(file_location)



        if current == '.txt':
            file.txt_to_bf(file_location)
        else:


            interpreter.run_code(file.read())
    else:
        interpreter.run_code(input("Input the code you wish to run:"))



if __name__ == "__main__":

    main()
