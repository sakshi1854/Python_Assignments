#Design automation script which accepts directory name and two file extensions from user.
#Rename all files with first file extension with the second file extension.
#Usage:DirectoryRename.py "Demo" ".txt" ".doc"
#Demo is the name of directory and .txt is the extension that we want to search and rename with .doc.
#After execution this script each .txt file gets renamed as .doc.

import sys
import os

def DirectoryRename(DirName,Ext1,Ext2):
    try:
        if not os.path.exists(DirName):
            print("Directory does not exists.")
            return 
        if not os.path.isdir(DirName):
            print("Invalid Directory name.")
            return 
        if not Ext1.startswith(".") or not Ext2.startswith("."):
            print("Invalid file extension format.")
            return 
        for FolderName,SubFolderName,FileName in os.walk(DirName):
            for fname in FileName:
                if fname.endswith(Ext1):
                    old_path=os.path.join(FolderName,fname)
                    new_name=fname.replace(Ext1,Ext2)
                    new_path=os.path.join(FolderName,new_name)
                    os.rename(old_path,new_path)
                    print(f"Renamed:{fname}->{new_name}")
    except Exception as e:
        print("Error occured:",e)

def main():
    if(len(sys.argv)<4):
        print("Invalid number of command line arguments.")
        return 
    DirectoryName=sys.argv[1]
    Extension1=sys.argv[2]
    Extension2=sys.argv[3]

    DirectoryRename(DirectoryName,Extension1,Extension2)



if __name__=="__main__":
    main()