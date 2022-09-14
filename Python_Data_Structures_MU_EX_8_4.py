'''8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append
 it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt'''

# open the file and read it
fname = input("Enter file name: ")
fh = open(fname, 'r')
# create list
lst = list()
# first for loop pulls line from fh and makes list of words in line
for line in fh:
    words = line.split()
    # second for loop iterates through each word pulled from list 
    ## checks if it's alread in lst and appends to lst if not
    for word in words:
        if word not in lst:
            lst.append(word)  
# sort the list (default is alphabetical order)
lst.sort()
print(lst)