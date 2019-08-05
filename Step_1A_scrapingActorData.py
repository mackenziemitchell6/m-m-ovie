#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:32:13 2019

@author: mackenziemitchell
"""

#importing any libraries we may need
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import pickle

#retrieving html from fandago
response=requests.get('https://www.fandango.com/famous-actors-and-actresses')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
#beginning to webscrape, peeling a few layers back
popCelebs=soup.findAll('div', {'class':'topperformers-row'})

#webscraping further and appending actors and their ranks to a list of dictionaries
rankedCelebs=[]
for celeb in popCelebs:
    name = celeb.findAll('a')[1].text
    rankedCelebs.append(name)
actors = []
i=1
for celeb in rankedCelebs:
    actors.append({'name':celeb, 'popularityRank':i})
    i+=1
actors

#Cleaning up the dictionary
popactorNames=[]
for celeb in rankedCelebs:
    popactorNames.append(celeb)
popactorNames
popularActors=[]
for actor in popactorNames:
    popularActors.append(actor.lstrip())
popularActors
actors

#storing the data in a pickle file
data=actors
F=open('popularActorsRanked.pkl','wb')
pickle.dump(data, F)
F.close()

#retrieving html from fanpagelist
onlinePres=[]
fbData=[]
socialActorNames=[]
#must create list of numbers in order to get data on further pages
pagenum=['1','2','3','4','5','6','7','8','9','10']
#loop through all the pages, get their html, and webscrape to get what we need
for page in pagenum:
    response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page'+page)
    soup=BeautifulSoup(response.content,'html.parser')
    soup.prettify
    facebookActors=soup.findAll('span',{'class':"title"})
    totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
    for actor in totalOnlinePres:
        onlinePres.append(actor.text)
    i=0
    #appending actors and their online following to a list of dictionaries
    for actor in facebookActors[0:20]:
        fbData.append({'name':actor.text,"Online following":onlinePres[i]})
        i+=1
        #getting a list of just the names, excluding online following
    for actor in facebookActors[0:20]:
        socialActorNames.append(actor.text)

socialActorNames
#storing data in a pickle file
data=fbData
data
F=open('socialMediaData.pkl','wb')
pickle.dump(data, F)
F.close()

#retrieving html from forbes
response=requests.get('https://www.forbes.com/sites/natalierobehmed/2017/08/22/full-list-the-worlds-highest-paid-actors-and-actresses-2017/#731b6e337515')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
#beginning to scrape
actorSalaryData=soup.findAll('p')[7:37]
actorSalaryData[2].text
actorSalaryList=[]
#getting just a list of the wealthy actor names, excluding their salary information
for actor in actorSalaryData:
    actorSalaryList.append(actor.text)
actorsAndSalaries=[]
#cleaning data so there are no $ in list
actorSalaryList
for actor in actorSalaryList:
    actorName, salary = actor[3:].split('$')
    actorsAndSalaries.append({'actorName':actorName.lstrip(),'salary':salary})
len(actorsAndSalaries)
#storing data in a pickle file
data=actorsAndSalaries
data
F=open('salaryData.pkl','wb')
pickle.dump(data, F)
F.close()
    
    
    
#The rest of the code here is simply preliminary cross-referencing to get an idea of what actors are on multiple lists
RichAndInfluencial=[]
for celeb in socialActorNames:
    for actor in actorSalaryList:
        if celeb in actor:
            RichAndInfluencial.append(celeb)
RichAndInfluencial

data=RichAndInfluencial
data
F=open('richSocialActors.pkl','wb')
pickle.dump(data, F)
F.close()

F1 = open('richSocialActors.pkl', 'rb')
d1 = pickle.load(F1)

popAndRich=[]
for actor in popactorNames:
    for celeb in actorSalaryList:
        if actor in celeb:
            popAndRich.append(actor)
popAndRich

data=popAndRich
data
F=open('popularRichActors.pkl','wb')
pickle.dump(data, F)
F.close()

popAndInfluencial=[]
for actor in socialActorNames:
    for celeb in popactorNames:
        if actor in celeb:
            popAndInfluencial.append(actor)
popAndInfluencial

data=popAndInfluencial
data
F=open('popularSocialActors.pkl','wb')
pickle.dump(data, F)
F.close()

popInfluRich=[]
for actor in popAndInfluencial:
    for celeb in popAndRich:
        if actor in celeb:
            popInfluRich.append(actor)
popInfluRich

data=popInfluRich
data
F=open('eliteActors.pkl','wb')
pickle.dump(data, F)
F.close()

## some line

