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
    """
    print("Welcome!")
    print("If you're trying to look for multiple words, please format it as [give, gave], otherwise you can put it in as \"give\"")
    print("To find a word from a spreadsheet or folder of spreadsheets, run python test3.py (insert word(s)) (insert file/folder name to find in)")
    print("Make sure to include .csv in your file name, otherwise the program will probably think that your csv file is a folder.")
    """
    args = sys.argv[1:]
    if len(args) != 2:
        print("not enough args :(")
        print("If you're trying to look for multiple words, please format it as \"give,gave\"")
        print("To find a word from a spreadsheet or folder of spreadsheets, run python test3.py (insert word(s)) (insert file/folder to find in)")
    else:
        if '.csv' in args[1]:
            listofwordsfromfile(args[0], args[1])
        else:
            wordfromfolder(args[0], args[1])
        
def wordfromfile(word, csvfile):
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
            wordfromfile(word, i)

    os.chdir('../')

def wordfromfolder(word, folder):
    """
    This function takes in a string, word, and a string, folder that's a folder containing csv files, and finds
    all entries in the csv file that match word.
    """
    os.chdir(folder)
    csvfiles = os.listdir()
    tables = []
    for i in csvfiles:
        if '.csv' in i:
            #wordfromfile(word, i)
        
            data = pd.read_csv(i)
            #data.fillna(' ', inplace=True)
            data = data.where(data.loc[:, 'English'].str.contains(word) == True).dropna()
            tables.append(data)
    final_data = pd.concat(tables, ignore_index=True)
    final_data.to_csv(word + folder + 'results.csv')
    print('Your file is: '+ word + folder + 'results.csv')
    
    os.chdir('../')

def listofwordsfromfile(words, csvfile):
    """
    This function takes in a list of strings, words, and a string file, that's either a folder containing csv files
    or a csv file, and it'll use findword or fromfolder to search for the specified words in the csv file(s).
    """
    wordsplit = words.split(',')
    data = pd.read_csv(csvfile)
    data.fillna(' ', inplace=True)
    tables = []
    for word in wordsplit:
        worddata = data.where(data.loc[:, 'English'].str.contains(word) == True).dropna()
        tables.append(worddata)

    final_data = pd.concat(tables, ignore_index=True)
    final_data.to_csv(words + csvfile.replace('.csv', '') + 'results.csv')
    print('Your file is: '+ words + csvfile.replace('.csv', '') + 'results.csv')


if __name__ == "__main__":
    main()