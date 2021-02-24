from modules import utils
from modules import file_with_functions
import os

if __name__ == '__main__':
# Test 1: get_file_names
    print("-----------------------")
    print("test 1: get_file_names")
    print("-----------------------")
    output_file_name = "files/output_get_file_names.txt"
    utils.get_file_names("files", output_file_name)
    file_with_functions.print_file_content('files/output_get_file_names.txt')

    # Test 2
    print("-----------------------")
    print("test 2: get_all_file_names")
    print("-----------------------")
    outputFileName = "files/output_get_all_file_names.txt"
    utils.get_all_file_names("files", outputFileName)
    file_with_functions.print_file_content('files/output_get_all_file_names.txt')

    # Test 3
    print("-----------------------")
    print("test 3: print_line_one")
    print("-----------------------")
    lst_files = ["files/output_get_all_file_names.txt"]
    utils.print_line_one(lst_files)


    # Test 4
    print("-----------------------")
    print("test 4: print_emails")
    print("-----------------------")
    lst_mails = ["files/email.txt"]
    print("\ne-mails in [files/email.txt]:\n")
    utils.print_emails(lst_mails)

    # Test 5
    print("-----------------------")
    print("test 5: write_headlines")
    print("-----------------------")
    outputFileName = "files/output_headlines.txt"
    lst_files = ["files/README_USE.md"]
    utils.write_headlines(lst_files, outputFileName)
    print("\nHEADLINES: ")
    file_with_functions.print_file_content('files/output_headlines.txt')
