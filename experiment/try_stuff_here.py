

#I was just experimenting on converting to and from binary number representations in python
def main():
    data = 0b0100000101100011

    length = 0

    while data - 2 ** length > 0:
        length +=2


    print(length)



    print(data.to_bytes(length // 8, byteorder='big'))






if __name__ == "__main__":
    main()