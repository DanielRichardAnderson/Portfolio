#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:22:30 2023

@author: danielanderson
"""
from bs4 import BeautifulSoup
from word2number import w2n
import pandas as pd
import requests
import time
import sys
import os
import itertools
import threading

# Function to print a loading animation
done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    

###########################
# Importing original HTML #
###########################
url = "https://books.toscrape.com/index.html?"

response = requests.get(url)

if response.status_code == 200:
    print("\nRequest was successful!")
else:
    print(f"Request failed with status code {response.status_code}")

soup = BeautifulSoup(response.text, 'lxml')


######################################
# Getting the data for the dataframe #
######################################
t = threading.Thread(target=animate)
t.start()

# Looping over the data from the main page.
link_list=[]
star_list=[]
title_list=[]
for article in soup.find_all('article', class_='product_pod'):
    try:
        link_list.append(article.div.a['href'])
    except (IndexError, KeyError, TypeError, ValueError) as e:
        print(f"Error extracting star rating: {e}")
        link_list.append(None)
        
    try:
        star_list.append(w2n.word_to_num(article.p['class'][1]))
    except (IndexError, KeyError, TypeError, ValueError) as e:
        print(f"Error extracting star rating: {e}")
        star_list.append(None)
        
    try:
        title_list.append(article.h3.a['title'])
    except(IndexError, KeyError, TypeError, ValueError) as e:
        print(f"Error extracting star rating: {e}")
        title_list.append(None)

# Looping over the data for each individual book.
# to get its description.    
blerb_list=[]
for link in link_list:
    # Getting each individual URL
    url = "https://books.toscrape.com/"+link
    # Getting the HTML for each book
    responseL = requests.get(url)
    responseL.encoding = 'utf-8'
    if responseL.status_code==200:
        pass
    else:
        print(f"Request failed with status code {responseL.status_code}")
    
    # Converting to soup object
    soupL = BeautifulSoup(responseL.text, 'lxml')
    
    # Parsing the HTML and adding it all toa list.
    try:
        description = soupL.find_all('meta')[2]['content']
        blerb_list.append(description)
    except (IndexError, KeyError, TypeError, ValueError) as e:
        print(f"Error extracting star rating: {e}")
        blerb_list.append(None)
        

##############################################
# Creating the dataframe to hold the results #
##############################################
df = pd.DataFrame()
df['title']=title_list
df['star-rating']=star_list
df['link']=link_list
df['blerb']=blerb_list

# Telling load animation to stop.
done = True


########################
# Saving the dataframe #
########################
csv_file_path = '/Users/danielanderson/Documents/python_files/scraped_file.csv'

# Check if the file already exists
if os.path.isfile(csv_file_path):
    overwrite = input("\nThe file already exists. Do you want to overwrite it? (y/n): ").lower()
    if overwrite == 'n':
        print("\nExiting without overwriting the file.")
    else:
        print("\nOverwriting the existing file.")
        df.to_csv(csv_file_path, index=False)
        print(f'Dataframe saved to {csv_file_path}')
else:
    df.to_csv(csv_file_path, index=False)
    print(f'\nDataframe saved to {csv_file_path}')

print('\nProgramme complete.\n')