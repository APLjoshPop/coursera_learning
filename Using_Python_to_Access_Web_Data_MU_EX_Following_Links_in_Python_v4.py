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

def get_page_hyperlinks(_url, position_in_list):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # get url
    url = _url
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the hyperlink tags
    hyperlink_tags = soup("a")

    #create variables
    hyperlink_list =[]

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
    
    return(' '.join(hyperlink_list[position_in_list]))

#Main
# get inputs
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

#Variables
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# count = 4
# position = 3

# url = "http://py4e-data.dr-chuck.net/known_by_Lottie.html"
# count = 7
# position = 18

list_of_urls = []

#While loop to iterate through get_page_hyperlinks the number of times we ask it to (var "count")
while count > 0:
    print("Retrieving: ",url)
    count -=1
    #call function get_page_hyperlinks and assign return of that function to url_retrieved
    url_retrieved = get_page_hyperlinks(url, (position -1))
    #make url for next pass in while loop the url_retrieved
    url = url_retrieved
    
    list_of_urls.append(url_retrieved)

#need to print the last url retrieved for assignments requested output
print("Retrieving: ",url)

#print the name of the person (var "answer") in the last url retrieved
last_url_retrieved = (list_of_urls[-1])
#the name is in the url, pull the name from the url and make it a string with join
answer = ' '.join(re.findall("_by_(.+).html",last_url_retrieved))
print(f'The answer to the assignment for this execution is "{answer}".')


# first_url = get_page_hyperlinks(url, (position -1))
# print(first_url)

# second_url = get_page_hyperlinks(first_url, 2)
# print(second_url)

# third_url = get_page_hyperlinks(second_url, 2)
# print(third_url)

# fourth_url = get_page_hyperlinks(third_url, 2)
# print(fourth_url)