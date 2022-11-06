'''
Counting Organizations

This application will read the mailbox data (mbox.txt) and count the number of email messages per organization 
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.

If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in
 the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the 
 data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is
 a balance between the number of operations you execute between commits and the importance of not losing the results of 
 operations that have not yet been committed. 
'''

# imports
import sqlite3
import re

# SQLlite setup
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# If there is already a table delete it
cur.execute('DROP TABLE IF EXISTS Counts')

# Creat a new table with colmns org and count
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# prompt user for a name for the file
fname = input('Enter file name: ')

# if no file nae is given it will default to naming the file mbox-short.txt
if (len(fname) < 1):
    fname = 'mbox.txt'

# open the file provided
file_handle = open(fname)
for line in file_handle:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    #domain = re.findall("(?<=@)[^.]+(?=\.)", email)
    domain = re.findall("(?<=@).+", email)
    print("domain is : ", domain)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain))
conn.commit()

# https://www.sqlite.org/lang_select.html
# select SUM(count), substr(email, instr(email, '@') + 1) as DOMAIN from Counts GROUP BY DOMAIN ORDER BY SUM(count) DESC;
#sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
#sqlstr = "SELECT SUM(count), SUBSTR(email, INSTR(email, '@') +1) AS domain FROM Counts GROUP BY domain ORDER BY SUM(count) DESC"
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'


for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
