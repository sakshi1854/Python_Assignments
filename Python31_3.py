#Design automation script which accept two directory names.copy all files from first first directory into second directory.second directory should be created at run time.
#Usage:DirectoryCopy.py "Demo" "Temp"
# Demo is the name of the directory which is the existing and contains file in it.we have to create new directory as temp and copy all files from Demo to Temp.

import sys
import os

def DirectoryCopy(src,dest):
    try:
        if not os.path.isdir(src):
            print("Source directory does not exists.")
            return 
        if not os.path.exists(dest):
            os.mkdir(dest)
        
        for file in os.listdir(src):
            src_path=os.path.join(src,file)
            dest_path=os.path.join(dest,file)

            if os.path.isfile(src_path):
                src_file=open(src_path,"rb")
                dest_file=open(dest_path,"wb")

                while True:
                    data=src_file.read(1024)
                    if not data:
                        break
                    dest_file.write(data)
                src_file.close()
                dest_file.close()
        print("Print All files copied successfully.")
    except Exception as e:
        print("Error:",e)


def main():
    if(len(sys.argv)<3):
        print("Invalid number of command line arguments.")
        return 
    DirectoryCopy(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()