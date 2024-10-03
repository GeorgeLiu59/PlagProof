#Preprocessor Directives
import os,sys

from plagiarismchecker import *

"""
This program takes user inputted text file(s), and either scrapes the web (top 4 websites) for similar information or compares it 
to another document. This program uses the machine learning library sklearn to transform 
the information from the websites into weighted arrays. The 'TfidVectorizer' and 'toarray' functions are part of the sklearn library.
These weighted arrays take context into account, taking the use of similar 
phrases and commonly used words into consideration. These arrays are then compared using a cosine similarity formula to calculate
the similarity value.
"""

def main():

    #Calls the class with all the code in it
    HomePage()

    sys.exit(0)

if (__name__=="__main__"):
    main()

