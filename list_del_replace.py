#!/usr/bin/python


__author__ = "Laura G. Macias"

from argparse import ArgumentParser
import csv

'''
Program to remove or replace elements contained a txt file.
Input text file provide by the < -list_in > option: elements separated by \n

USAGE options:

 - Delete: elements provided by -replace option will be removed from input text file
 
 python list_del_replace.py -list_in input_list.txt -del -changes elements_to_change.txt
 
 elements_to_change.txt --> elements separated by \n
 Example:
 gene345
 G87
 tag76
 
 Elements  gene345, G87 and tag76 will be removed from input text file
 
 
 - Replace: 
 
 python list_del_replace.py -list_in input_list.txt -repl -changes elements_to_change_and_replacements.txt
 
 elements_to_change_and_replacements.txt --> elements separated by: element2find \t replacement
 Example:
 gene345    G0140
 G87    G0150
 tag76  G0160
 
 Elements  gene345, G87 and tag76 will be replaced by G0140, G0150, G0160 respectively.
 
 OUTPUT: 
 Final list will be written in the standard output. To save new list:
 Example:
 
 python list_del_replace.py -list_in input_list.txt -del -changes elements_to_change.txt > new_list.txt
 
 
 
'''


def main():
    parser = ArgumentParser()
    parser.add_argument("-list_in", dest="file_list", help="input file containing list of elements", type=str)
    parser.add_argument("-changes", dest="list_changes", help="text file with elements to be removed or change", type=str)
    parser.add_argument("-repl", dest="replace", help="replace elemnts in input list", action="store_true", default=False)
    parser.add_argument("-del", dest="delete",help="remove elements in input list", action="store_true", default=True)

    args = parser.parse_args()

    # Option: replace
    if args.replace:
        replacements = {}
        with open(args.list_changes, "r") as input_handle:
            csvreader = csv.reader(input_handle,delimiter="\t")
            for row in csvreader:
                replacements[row[0]] = row[1]

        elements = []
        with open(args.file_list, "r") as list_in:
            for line in list_in:
                e = line.strip()
                if e in replacements.keys():
                    elements.append(replacements[e])
                else:
                    elements.append(e)


        for x in elements:
            print(x)

    # Option: delete
    if args.delete:
        del_elements = []
        with open(args.list_changes, "r") as input_handle:
            for line in input_handle:
                e = line.strip()
                del_elements.append(e)

        with open(args.file_list, "r") as list_in:
            for line in list_in:
                e = line.strip()
                if e not in del_elements:
                    print(e)


if __name__ == "__main__":
    main()


