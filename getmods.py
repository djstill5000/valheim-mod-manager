#!/usr/bin/env python3

import requests
import time
import warnings
import csv
import os
import shutil
from bs4 import BeautifulSoup
from tqdm import tqdm
from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

warnings.simplefilter("ignore")

chunk_size = 1024

modsdir = str(config['PARAMETERS']['mods_dir'])
modscsv = str(config['PARAMETERS']['mods_csv'])

#Parse Webpage and return newest mod version
def getversions(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        if type(link.get('href')) == str:
            if 'https://thunderstore.io/package/download/' in link.get('href'):
                links.append(link.get('href'))

    return links[0]

#Truncates and formats mod name to be legible in the progress bar
def truncate(url, iterations):
    if iterations == 3:
        return url
    else:
        newurl = url[0:url.rfind('/')]
        return truncate(newurl, iterations+1)

#Scans requested mods and formats them and stores into a list
def read_csv(file_path):
    data_list = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            # Strip leading and trailing whitespace and exclude empty strings
            cleaned_row = [element.strip() for element in row if element.strip()]
            data_list.extend(cleaned_row)

    return data_list


#Removes old mods if mods.csv has been changed
def emptyfolder(modsdir):
    dirs = os.listdir(modsdir)

    for doc in dirs:
        actualdir = modsdir + '/' + doc
        print(modsdir + '/' + doc)
        if doc.endswith('.dll'):
            pass
        elif os.path.isfile(actualdir):
            os.remove(actualdir)
        elif os.path.isdir(actualdir):
            shutil.rmtree(actualdir)


#Deletes the zipped folders from the newly created mods
def emptyfolder2(modsdir):
    dirs = os.listdir(modsdir)

    for doc in dirs:
        actualdir = modsdir + '/' + doc
        if doc.endswith('.zip'):
            os.remove(actualdir)
        else:
            pass


emptyfolder(modsdir)
urls = read_csv(modscsv)


#Adds new mods to the mods directory
for i in range(len(urls)):

    modversion = getversions(urls[i])
    req = requests.get(modversion, stream = True)
    filename = req.url[modversion.rfind('/'):]
    index_one = truncate(modversion,0)
    mod = modversion[len(index_one)+1:-1]
    filesize = int(req.headers['content-length'])
    fileloc = modsdir + '/' + filename

    #Creates loading bar in terminal
    with open(fileloc, 'wb') as f:
        for chunk in tqdm(iterable = req.iter_content(chunk_size=chunk_size), total = filesize/chunk_size, unit = 'MB', ascii = '-#', desc = mod):
            if chunk:
                f.write(chunk)
    newpath = os.path.join(modsdir, os.path.splitext(filename)[0])
    os.makedirs(newpath)
    shutil.unpack_archive(fileloc, modsdir + '/' + os.path.splitext(filename)[0])

emptyfolder2(modsdir)
