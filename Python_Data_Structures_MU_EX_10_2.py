"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

# Note: working off of code used in 9.4 since this would seem to be an expansion from that
# open file and read it.
# file_name = input("Enter file name: ")
file_name = "mbox-short.txt"
file_handle = open(file_name, "r")

# create variables
hours_count = 0
hours = dict()

# read file line by line looking for 'From'
for line in file_handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()

    # create dictionary based counter to count number of times a specific time occures
    # grab the time it will be the 6th element in the words list
    time = words[5]
    # get the hour from the time by spliting time by ":" making it a list (or is it a touple?)...
    # ...and grabbing the hour (it will be the first item in the list)
    time = time.split(":")
    print(time)  # ??? Show Cory
    hour = time[0]

    hours[hour] = hours.get(hour, 0) + 1
    hours_count += 1

# need for loop to print hours, will sort in for statement to create correct format for Desired Output
for hour, hour_count in sorted(hours.items()):
    print(hour, hour_count)
