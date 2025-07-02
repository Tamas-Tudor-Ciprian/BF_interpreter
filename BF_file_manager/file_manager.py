import struct

import os


BF_EXTENSION = '.bf'



def ensure_ext(path):
    base, current = os.path.splitext(path)
    if current.lower() != BF_EXTENSION:
        return base + BF_EXTENSION
    return path





class BF_file():
    MAGIC = b'BF01'
    HEADER = '>4sI'

    def __init__(self,file_path):
        self.__file_path = ensure_ext(file_path)

    def write(self,data):
        payload = data.encode('utf-8')
        with open(self.__file_path,'wb') as f:
            f.write(struct.pack(BF_file.HEADER,BF_file.MAGIC,len(payload)))
            f.write(payload)

    def read(self):
        with open(self.__file_path,'rb') as f:
            magic, length = struct.unpack(BF_file.HEADER,f.read(8))
            if magic != BF_file.MAGIC:
                raise ValueError("Not a BF file!")
            payload = f.read(length)

            return payload.decode('utf-8')

    def txt_to_bf(self,text_file):
        with open(text_file,'r') as f:
            data = f.read()
            filtered_data = "".join(ch for ch in data if ch in "><+-.,[]")
            self.write(filtered_data)


    def get_path(self):
        return self.__file_path
