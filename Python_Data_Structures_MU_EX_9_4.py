'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

#Note: working off of code used in 8_5 since this would seem to be an expansion from that
# open file and read it.
#fname = input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname, 'r')

# create variables
count = 0
names= dict()

# read file line by line looking for 'From' 
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    
    #create dictionary based counter to count number of times a name occures
    name = (words[1])
    names[name] = names.get(name, 0) +1
    count = count +1

    #Find the name in the dictoinary with the largest count
    largest_key = None
    largest_value = 0
    for key,value in names.items():
        if value > largest_value:
            largest_key = key
            largest_value = value
            print (largest_key, largest_value)
    
print(names)
print (largest_key, largest_value)
    
