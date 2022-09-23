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
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the hyperlink tags
hyperlink_tags = soup("a")

#variables
hyperlink_list = []
count = 4
position = 2

def get_page_hyperlinks(hyperlink_tags, position_in_list):
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
    return(hyperlink_list[position_in_list])

new_hyperlink_tags = ' '.join((get_page_hyperlinks("http://py4e-data.dr-chuck.net/known_by_Fikret.html", position)))
while count > 0:
    new_hyperlink_tags = ' '.join((get_page_hyperlinks(new_hyperlink_tags, position)))
    print(new_hyperlink_tags)
    
    count = count - 1
