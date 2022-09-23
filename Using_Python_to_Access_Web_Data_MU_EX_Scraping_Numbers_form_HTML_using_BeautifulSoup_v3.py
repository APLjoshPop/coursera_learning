'''
Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Lottie.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: S
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

Sample execution

Here is a sample execution of a solution:

$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
The answer to the assignment for this execution is "Anayah".
'''
# Using code from Extracting_Data_w_Regular_Expressions assignment as base for this project

# imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get url
# url = input("Enter URL: ")
url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

#variables
hyperlink_list = []
count = 4
position = 2

#While loop to crawl through web pages
while count > 0:
    # open url
    print("ran 1: ", count, url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    #print('soup:', soup)

    # Retrieve all of the hyperlink tags
    hyperlink_tags = soup("a")

    # read each hyperlink tag
    # Create a list of the hyperlinks
    for content in hyperlink_tags:
        #check if the hyperlink_tag (content) is a string, if not convert to string
        if isinstance(content,str) == False:
            #convert content type from soup to string
            content_string = str(content)
        else:
            content_string = content

        #search link for hyperlink and add it to a list of hyperlinks
        hyperlink = re.findall("href=\"(.+)\"",content_string)
        #print(hyperlink)
        hyperlink_list.append(hyperlink)
        #print(hyperlink_list)

    #reset url variable
    # @Cory why doesn't the code below work? convirt list item to string and set as value of var url
    # url = str(hyperlink_list[2])

    url = ' '.join(hyperlink_list[2])
    print('ran 2: ', count, url)  
    count = count-1



        
        

#print(hyperlink_list[position])