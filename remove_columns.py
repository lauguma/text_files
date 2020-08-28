#!/usr/bin/python

import pandas as pd
from argparse import ArgumentParser



def main():

    parser = ArgumentParser()
    parser.add_argument("-table", dest="table_input", help="input table", type=str)
    parser.add_argument("-cols", dest="columns", help="text file containing columns to be removed", type=str)
    parser.add_argument("-out", dest="table_output", help="output table name", type=str)
    args = parser.parse_args()


    df = pd.read_csv(args.table_input, sep="\t", encoding='utf-8')


    # Column names to be removed

    cols = []
    with open(args.columns,"r") as f_in:
        for line in f_in:
            cols.append(line.strip())

    new_df = df.drop(cols,1)

    # save new df
    new_df.to_csv(args.table_output,index=False, sep="\t", encoding='utf-8')


    print("Nr. columns input table: ",len(df.columns))
    print("Nr. columns output table: ",len(new_df.columns))







if __name__ == "__main__":
    main()
