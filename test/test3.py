import sys
import pandas as pd
import os

def main():
    """
    args = sys.argv[1:]
    if len(args) == 1 and isinstance(args[0], str):
        print("Hi!" + args[0])
    else:
        print("wrong num args :(")
    """
    args = sys.argv[1:]
    if len(args) != 2:
        print("wrong num args :(")
        print("To find a word from a spreadsheet or folder of spreadsheets, run python test3.py (insert word) (insert file/folder to find in)")
    else:
        if '.csv' in args[1]:
            findword(args[0], args[1])
        else:
            fromfolder(args[0], args[1])

def findword(word, csvfile):
    """
    This function takes in a string, word, and finds all entries in the English column that match it in the
    csvfile, which is a string of the filename
    """
    data = pd.read_csv(csvfile)
    data.fillna(' ', inplace=True)
    data = data.where(data.loc[:, 'English'].str.contains(word) == True).dropna()
    data.to_csv(word + csvfile.replace('.csv', '') + 'results.csv')
    print('Your file is: '+ word + csvfile.replace('.csv', '') + 'results.csv')

def fromfolder(word, folder):
    """
    This function takes in a string, word, and a string, folder that's a folder containing csv files, and finds
    all entries in the csv file that match word.
    """
    os.chdir(folder)
    csvfiles = os.listdir()
    for i in csvfiles:
        if '.csv' in i:
            findword(word, i)

    os.chdir('../')

if __name__ == "__main__":
    main()