import os,sys

import math as mt

from mpm import *

import tkinter as tk

from tkinter import scrolledtext

from tkinter import ttk

import string

from googlesearch import search #python3 -m pip install googlesearch-python

import pandas as pd #pip install pandas

import numpy as np #pip install numpy

from bs4 import BeautifulSoup #pip install bs4

import requests

from sklearn.feature_extraction.text import TfidfVectorizer #pip install numpy, pip install scipy, pip install -U scikit-learn

class HomePage:

    def __init__(self):
        #Creating and naming the self.window, making background color
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.root.title("Document Plagiarism Calculator")
        self.root.configure(background = "white")

        #Putting in a photo for the title
        path = "DocumentSim.png" 
        p1 = tk.PhotoImage(file=path)
        tk.Label (self.root, image = p1, bg = "white") .place(x = 0, y = 20)

        #Instructions Labels
        self.instructions = tk.Label(self.root, text = " Choose Method of Comparison ", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 126, y = 150)

        #Button that leads to online comparison class
        self.intbutton = ttk.Button (self.root, text=' Document to Online ', command = lambda: self.newWindow(InternetChecker).pack())

        self.intbutton.place(x = 110, y = 200)

        #Button that leads to document comparison class
        self.docbutton = ttk.Button (self.root, text='Document to Document', command = lambda: self.newWindow(DocumentChecker).pack())
        self.docbutton.place(x = 250, y = 200)

        self.root.mainloop()
    
    #Function that opens up a new window 
    def newWindow(self, cls):
        try:
            #Ensures that only one of each window can be open at a single time
            if (self.new.state() == "normal"):
                self.new.focus()

        except:

            #Creates new window
            self.new = tk.Toplevel(self.root)
            cls(self.new)
        
#Class for Document-Document similarity
class DocumentChecker:

    def __init__(self, rt):
        #Creating and naming the self.window, making background color
        self.window = rt
        self.window.geometry("1152x648")
        self.window.title("Document Plagiarism Calculator")
        self.window.configure(background = "white")

        #Putting in a photo for the title
        path = "DocumentSim.png" 
        p1 = tk.PhotoImage(file=path)
        tk.Label (self.window, image = p1, bg = "white") .place(x = 0, y = 20)

        #Button to open a text file
        self.openfile = ttk.Button (self.window, text='Open', command = self.open) .place(x = 95, y = 165)

        #Button to calculate similarity
        self.calculate = ttk.Button (self.window, text='Calculate Similarity', command = self.check) .place(x = 35, y = 605)

        #Button to clear all text boxes and lists
        self.clear = ttk.Button (self.window, text='Clear All', command = self.clear) .place(x = 185, y = 605)

        #Instructions Labels
        self.instructions = tk.Label(self.window, text = "Choose Document 1", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 60, y = 115)

        self.chose = tk.Label(self.window, text = "Chosen Text: ", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 83, y = 220)

        #Scrolled txt box to contain the user inputted text file
        self.chosen_txt = scrolledtext.ScrolledText(self.window, width = 33, height = 20, font = ("Roboto", 11))
        self.chosen_txt.place(x = 0, y = 255)

        #Instructions Labels
        self.instructions2 = tk.Label(self.window, text = "Choose Document 2", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 370, y = 115)
        
        #Button to open a text file
        self.openfile2 = ttk.Button (self.window, text='Open', command = self.open2) .place(x = 410, y = 165)

        self.chose2 = tk.Label(self.window, text = "Chosen Text: ", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 393, y = 220)

        #Scrolled txt box to contain the user inputted text file
        self.chosen_txt2 = scrolledtext.ScrolledText(self.window, width = 33, height = 20, font = ("Roboto", 11))
        self.chosen_txt2.place(x = 310, y = 255)

        #Label to indicate information of the 1st website
        self.web1 = tk.Label(self.window, text = "Document Similarity Percentage", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 720, y = 50)

        #Text boxes to contain the similarity values found
        self.sim1 = tk.Text(self.window, bg = "white", fg = "#092aa5", highlightthickness = 0, borderwidth=0, width = 16, height = 1, font = ("Roboto", 15, 'bold'))
        self.sim1.place(x = 755, y = 250)

        self.window.mainloop()

    #List to Contain the Websites Gotten From Query 
    urllist = []

    #List to Contain the Words From the Websites
    readlist = []

    #List to Contain the Similarity Values Between the Document and Websites
    similarityvals = []

    websitesim = dict()

    #Open file function for first text file
    def open(self, event = None):

        #Prompts user to choose a file and gets location of the file
        self.filepath = filedialog.askopenfilename(title = "Choose a Document to Compare")

        #Opens the user chosen file in read mode
        file = open(self.filepath, 'r')

        #Reads the user chosen file
        docread = file.read()

        #Inserts the read text file into a text box
        self.chosen_txt.insert(tk.END, docread)
        
        file.close()

    #Open file function for second text file
    def open2(self, event = None):

        #Prompts user to choose a file and gets location of the file
        self.filepath = filedialog.askopenfilename(title = "Choose a Document to Compare")

        #Opens the user chosen file in read mode
        file = open(self.filepath, 'r')

        #Reads the user chosen file
        docread = file.read()

        #Inserts the read text file into a text box
        self.chosen_txt2.insert(tk.END, docread)
        
        file.close()

    def check(self, event = None):

        #Gets the text from the document text box
        selectedtext = clean(self.chosen_txt.get("1.0", 'end-0c'))
        
        #Removes all punctuation from the gotten text
        selectedtext = selectedtext.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

        #Gets the text from the document text box
        selectedtext2 = clean(self.chosen_txt2.get("1.0", 'end-0c'))
        
        #Removes all punctuation from the gotten text
        selectedtext2 = selectedtext2.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
        
        #Appends the two entries to a list
        self.readlist.append(selectedtext)

        self.readlist.append(selectedtext2)

        #Setting up the vectorizer
        vctor = TfidfVectorizer()

        #Converts the gathered text from the read websites to a weighted array
        X = vctor.fit_transform(self.readlist)
        arr = X.toarray()

        #Puts title, url, and similarity information into the gui
        self.sim1.insert(tk.END, f"{round(similarity(arr[0],arr[1])*100)}% Similarity")
        
    def clear(self, event = None):

        #Deletes all the info in every text box of the gui
        self.chosen_txt.delete('1.0', tk.END)

        #Deletes all the info in every text box of the gui
        self.chosen_txt2.delete('1.0', tk.END)

        #Deletes all info in similarity values
        self.sim1.delete('1.0', tk.END)

        #Clearing all the lists used in the program
        self.urllist.clear()

        self.readlist.clear() 

        self.similarityvals.clear()

        self.websitesim.clear()

#Class for Document-Internet Similarity
class InternetChecker:

    def __init__(self, rt):
        #Creating and naming the self.window, making background color
        self.window = rt
        self.window.geometry("1152x648")
        self.window.title("Document Plagiarism Calculator")
        self.window.configure(background = "white")

        #Putting in a photo for the title
        path = "DocumentSim.png" 
        p1 = tk.PhotoImage(file=path)
        tk.Label (self.window, image = p1, bg = "white") .place(x = 0, y = 20)

        #Button to open a text file
        self.openfile = ttk.Button (self.window, text='Open', command = self.open) .place(x = 95, y = 165)

        #Button to calculate similarity
        self.calculate = ttk.Button (self.window, text='Calculate Similarity', command = self.check) .place(x = 35, y = 605)

        #Button to clear all text boxes and lists
        self.clear = ttk.Button (self.window, text='Clear All', command = self.clear) .place(x = 185, y = 605)

        #Instructions Labels
        self.instructions = tk.Label(self.window, text = "Choose a Text File to Scan Similarity", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 8, y = 115)

        self.chose = tk.Label(self.window, text = "Chosen Text: ", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 83, y = 220)

        #Label to indicate information of the 1st website
        self.web1 = tk.Label(self.window, text = "Website 1 ", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 300, y = 26)

        #Text box to contain information about the 1st website
        self.web1info = tk.Text(self.window, bg = "white", highlightthickness = 0, borderwidth=0, width = 48, height = 14, font = ("Roboto", 11))

        self.web1info.place(x = 300, y = 52)

        #Label to indicate information of the 2nd website
        self.web2 = tk.Label(self.window, text = "Website 2 ", bg = "white", fg = "#092aa5",font = ("Roboto", 11, 'bold') ) .place(x = 740, y = 26)

        #Text box to contain information about the 2nd website
        self.web2info = tk.Text(self.window, bg = "white", highlightthickness = 0, borderwidth=0, width = 48, height = 14, font = ("Roboto", 11))

        self.web2info.place(x = 740, y = 52)

        #Scrolled txt box to contain the user inputted text file
        self.chosen_txt = scrolledtext.ScrolledText(self.window, width = 33, height = 20, font = ("Roboto", 11))
        self.chosen_txt.place(x = 0, y = 255)

        #Text boxes to contain the similarity values found
        self.sim1 = tk.Text(self.window, bg = "white", fg = "#092aa5", highlightthickness = 0, borderwidth=0, width = 16, height = 1, font = ("Roboto", 15, 'bold'))
        self.sim1.place(x = 405, y = 250)

        self.sim2 = tk.Text(self.window, bg = "white", fg = "#092aa5", highlightthickness = 0, borderwidth=0, width = 16, height = 1, font = ("Roboto", 15, 'bold'))
        self.sim2.place(x = 850, y = 250)

        self.window.mainloop()

    #List to Contain the Websites Gotten From Query 
    urllist = []

    #List to Contain the Words From the Websites
    readlist = []

    #List to Contain the Similarity Values Between the Document and Websites
    similarityvals = []

    websitesim = dict()

    def open(self, event = None):

        #Prompts user to choose a file and gets location of the file
        self.filepath = filedialog.askopenfilename(title = "Choose a Document to Compare")

        #Opens the user chosen file in read mode
        file = open(self.filepath, 'r')

        #Reads the user chosen file
        docread = file.read()

        #Inserts the read text file into a text box
        self.chosen_txt.insert(tk.END, docread)
        
        file.close()

    def check(self, event = None):

        #Gets the text from the document text box
        selectedtext = clean(self.chosen_txt.get("1.0", 'end-0c'))
        
        #Removes all punctuation from the gotten text
        selectedtext = selectedtext.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

        #Puts the read text into the read list
        self.readlist.append(selectedtext)

        #Searches up the top 10 results relating to the text, appends to list
        for link in search(selectedtext, tld="co.in", num = 2, stop = 2, pause = 1):
            self.urllist.append(link)

        #Puts the read websites into the read list
        for url in self.urllist:
            self.readlist.append(readwebsite(url))

        #Removes all blank values from the list
        self.readlist = list(filter(None,self.readlist))

        #Compares every website array to the original text and calculates similarity
        for i in range(1,len(self.readlist)):
 
            #Setting up the vectorizer
            vctor = TfidfVectorizer()
 
            temp = [self.readlist[0],self.readlist[i]]
 
            #Converts the gathered text from the read websites to a weighted array
            wtemp = vctor.fit_transform(temp)
 
            arr = wtemp.toarray()
 
            #Uses similarity procedure to find similarity between the reference array and current array
            self.similarityvals.append(similarity(arr[0],arr[1]))

            print(similarity(arr[0],arr[1]))


        #Puts similarity values corresponding to urls inside of a dictionary
        for url in self.urllist:
            for simval in self.similarityvals:
                self.websitesim[url] = round(100*simval)
                self.similarityvals.remove(simval)
                break 

        #Sorts the entire dictionary from greatest to least
        sortedvals = sorted(self.websitesim.values(), reverse = True)

        sortedsim = dict()

        for val in sortedvals:
            for key in self.websitesim.keys():
                if (self.websitesim[key] == val):
                    sortedsim[key] = self.websitesim[key]

        #Setting up the requests to get the urls from the top 4 similar websites
        reqs1 = requests.get(tuple(sortedsim.keys())[0])
  
        soup1 = BeautifulSoup(reqs1.text, 'html.parser')

        reqs2 = requests.get(tuple(sortedsim.keys())[1])
  
        soup2 = BeautifulSoup(reqs2.text, 'html.parser')

        #Puts title, url, and similarity information into the gui

        #Writes title of the first website if found
        try:
            for title in soup1.find_all('title'):
                self.web1info.insert(tk.END, f"Title: {title.get_text()}")
        except:
             self.web1info.insert(tk.END, f"Title: No Title Found")

        self.web1info.insert(tk.END, f"\n\nURL: {tuple(sortedsim.keys())[0]}")
        self.sim1.insert(tk.END, f"{tuple(sortedsim.values())[0]}% Similarity")

        #Writes title of the second website if found
        try:
            for title in soup2.find_all('title'):
                self.web2info.insert(tk.END, f"Title: {title.get_text()}")
        except:
             self.web2info.insert(tk.END, f"Title: No Title Found")

        self.web2info.insert(tk.END, f"\n\nURL: {tuple(sortedsim.keys())[1]}")
        self.sim2.insert(tk.END, f"{tuple(sortedsim.values())[1]}% Similarity")
        
    def clear(self, event = None):

        #Deletes all the info in every text box of the gui
        self.chosen_txt.delete('1.0', tk.END)

        self.web1info.delete('1.0', tk.END)

        self.web2info.delete('1.0', tk.END)

        self.sim1.delete('1.0', tk.END)

        self.sim2.delete('1.0', tk.END)

        #Clearing all the lists used in the program
        self.urllist.clear()

        self.readlist.clear() 

        self.similarityvals.clear()

        self.websitesim.clear()
