from bs4 import BeautifulSoup

from collections import Counter

import os 

from tkinter import filedialog

import string

from urllib.request import Request, urlopen

from sklearn.feature_extraction.text import TfidfVectorizer #pip install numpy, pip install scipy, pip install -U scikit-learn

import math

#Procedure to find the dot product of any iterable
def dotp(X,Y):

    #Ensures that the lenghts of the two iterables inputted are more than 0 to prevent errors when zipping
    if (len(X) > 0 and len(Y) > 0):

        #Solves for dot product of elements in the iterables
        return (sum(x*y for x,y in zip(X,Y)))
    else:

        #Returns 0 for the similarity value
        return 0

#Procedure to calculate similarity by plugging in 2 documents
def similarity(txt1,txt2):

    if (dotp(txt1,txt2) == 0):

        #Returns 0 as the similarity value, as there are missing documents
        return 0
    else:
        #Plugs the dot product into the cosine similarity formula to return the similarity value
        return dotp(txt1,txt2) / (math.sqrt(dotp(txt1,txt1)) * math.sqrt(dotp(txt2,txt2)))

#Function to completely clean text and just return lowercase ascii characters
def clean(txt):
    #Strips the text of white space, turns it all lowercase, and removes line breaks for efficiency
    editedtext = txt.strip().lower().replace("\n","")

    #Puts the editedtext into a translation table to remove all punctuation
    editedtext = editedtext.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

    #Removes all not ascii characters from the text
    editedtext = ''.join([i if ord(i) < 128 else ' ' for i in editedtext])

    return editedtext

#Function to read off of a website and return the text gotten
def readwebsite(url):

    #Request that uses headers to simulate an actual session
    rq = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'})

    #Opens up the url if it can
    try:
        page = urlopen(rq)

    except:
        return 

    #Reads the entire website
    html = page.read().decode("utf-8")

    #Goes through the html to get all the content
    websitetext = BeautifulSoup(html, "html.parser")

    #Gets all text from the webpage content
    text = websitetext.get_text()

    #Returns a cleaned version of the text from the website
    return clean(text)


