from bs4 import BeautifulSoup   #importing the necessary libraries
import requests
import pandas as pd


#creating empty lists for storing the data
urls = []
ques = []
ans = []
views = []


#iterating the loop for the first "n" pages
n = int(input("Enter the number of pages to scrape:  "))

i = 00
for itr in range(n):
  url = 'https://thistudy.com/index.php?board=162.' + str(i)    #generating the links for first "n" pages
  req = requests.get(url)
  soup = BeautifulSoup(req.text, 'html.parser')

  for link in soup.find_all('a'):
      if "topic" in link["href"]:   #searching for the particular links for the questions
          urls.append(link.get("href"))
  i += 20


#extracting the data from the links of questions which we extracted above
#looping it to check for all the links
for link in urls:
    url = link
    req = requests.get(url)   #requesting the url
    soup1 = BeautifulSoup(req.text, 'html.parser')    #parsing it using html parser


    #extracting the question
    q = soup1.find("div", id=True, itemprop=True)
    ques.append(q.text.strip())   #storing the data in "ques" list


    #extracting the answer
    a = soup1.find("div", itemprop="text")
    ans.append(a.text.strip())    #storing the data in "ans" list


    #extracting the views
    v = soup1.find(class_="inline-block mbottom10 info-panel")
    item = v.text.strip().split()
    views.append(item[1])   #storing the data in "views" list


#creating the DataFrame to store the data in a csv format
df = pd.DataFrame({'Url': urls,   #assigning the data
                  'Question': ques,    #assigning the data    
                  'Answer': ans,   #assigning the data   
                  'Views': views})    #assigning the data


df.to_csv("data.csv")   #saving the data