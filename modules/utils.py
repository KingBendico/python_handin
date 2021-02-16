import os
import re
                
def get_file_names(folderpath, output_file):
    lst = os.listdir(folderpath)
    with open(output_file, 'w') as file_object:
        for line in lst:
            file_object.write(line + "\n")
    

def get_all_file_names(path, output_file):
    lst = []
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            lst.append(os.path.join(root, name)[len(path):])
        for name in directories:
            lst.append(os.path.join(root, name)[len(path):])
    with open(output_file, 'w') as file_object:
        for line in lst:
            file_object.write(line + "\n")
    

def print_line_one(file_names):
    for file in file_names:
        with open(file,'r') as file_object:
            print("\nFirst line in " + "\""+file + "\":\n" + "\n" + file_object.readlines()[0])
    
def print_emails(file_names):
    for file in file_names:
        with open(file,'r') as file_object:
            for line in file_object.readlines():
                if "@" in line:
                    print(line)
                   # print("File: " + file + "\n" + line)

def write_headlines(md_files, out):
    new_list = []
    for files in md_files:
        with open(files, "r") as f:
            for line in f:
                if re.search("^#", line):
                    new_list.append(line)
                    with open(out, "w") as o:
                        for el in new_list:
                            o.write(el)         
                
                