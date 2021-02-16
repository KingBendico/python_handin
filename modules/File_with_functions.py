import argparse
import csv
parser = argparse.ArgumentParser(description='A program to read from an input file, and either write it out in the console, or to an output file')

def print_file_content(file):
    with open(file,'r') as file_object:
        fileText = file_object.read()
        print(fileText)
        
def write_list_to_file(output_file, lst):
      with open(output_file, 'w') as file_object:
        for el in lst:
            file_object.write("\n".join(el) + "\n")    
                
def write_lines_to_file(output_file, *strings):
    # print(lst)
    with open(output_file, "w") as o:
        for el in strings:
                o.write(el + "\n")
                
def write_csv(input_csv_file, output_csv_file):
      with open(output_csv_file, 'w') as file_object:
        for el in input_csv_file:
            file_object.write(",".join(el) + "\n")                  
        
def read_csv(input_file):
    with open(input_file, "r") as f:
        new_list = []
        csv_reader = csv.reader(f)
        for row in csv_reader:
            new_list.append(row)

    return new_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that writes and reads from a csv file')
    parser.add_argument('-i', dest="input_file", default=True, help='Name of the input file. Must be in the same directory as this file.')
    parser.add_argument('-o', dest="output_file", default=None, help='name of the output file.')
    args = parser.parse_args()

    if args.output_file:
        output_csv_file = args.output_file
        input_csv_file = read_csv(args.input_file)
        write_csv(input_csv_file, output_csv_file)

   
    else:
        print_file_content(args.input_file)
        