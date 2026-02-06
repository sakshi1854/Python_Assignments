#Design automation script which accept two directory names and one file extension.copy all files with the specified extension from first directory into second directory.
# Second directory should be created at runtime.
# Usage:DirectoryCopyExt.py "Demo" "Temp" ".exe"
# Demo is the name of directory which is existing and contains files in it.we have to create new directory as temp and copy all files with the extension .exe from Demo to Temp.


import sys
import os

def DirectoryCopyExt(src,dest,ext):
    try:
        if not os.path.isdir(src):
            print("Source directory does not exists")
            return 
        if not os.path.exists(dest):
            os.mkdir(dest)
        for file in os.listdir(src):
            if file.endswith(ext):
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
        print("All",ext,"files copied successfully.")
    except Exception as e:
        print("Error:",e)

def main():
    if(len(sys.argv)<4):
        print("Invalid number of command line arguments:")
        return 
    DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])



if __name__=="__main__":
    main()