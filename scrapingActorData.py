#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:32:13 2019

@author: mackenziemitchell
"""

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import pickle

response=requests.get('https://www.fandango.com/famous-actors-and-actresses')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
popCelebs=soup.findAll('div', {'class':'topperformers-row'})

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

popactorNames=[]
for celeb in rankedCelebs:
    popactorNames.append(celeb)
popactorNames
popularActors=[]
for actor in popactorNames:
    popularActors.append(actor.lstrip())
popularActors
actors

data=actors
F=open('popularActorsRanked.pkl','wb')
pickle.dump(data, F)
F.close()

onlinePres=[]
fbData=[]
socialActorNames=[]
pagenum=['1','2','3','4','5','6','7','8','9','10']
for page in pagenum:
    response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page'+page)
    soup=BeautifulSoup(response.content,'html.parser')
    soup.prettify
    facebookActors=soup.findAll('span',{'class':"title"})
    totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
    for actor in totalOnlinePres:
        onlinePres.append(actor.text)
    i=0
    for actor in facebookActors[0:20]:
        fbData.append({'name':actor.text,"Online following":onlinePres[i]})
        i+=1
    for actor in facebookActors[0:20]:
        socialActorNames.append(actor.text)

socialActorNames

data=fbData
data
F=open('socialMediaData.pkl','wb')
pickle.dump(data, F)
F.close()

response=requests.get('https://www.forbes.com/sites/natalierobehmed/2017/08/22/full-list-the-worlds-highest-paid-actors-and-actresses-2017/#731b6e337515')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
actorSalaryData=soup.findAll('p')[7:37]
actorSalaryData[2].text
actorSalaryList=[]
for actor in actorSalaryData:
    actorSalaryList.append(actor.text)
actorsAndSalaries=[]

actorSalaryList
for actor in actorSalaryList:
    actorName, salary = actor[3:].split('$')
    actorsAndSalaries.append({'actorName':actorName.lstrip(),'salary':salary})
len(actorsAndSalaries)

richActorNames=[]
for actor in actorsAndSalaries:
    richActorNames.append(actor['actorName'].lstrip())
richActorNames
data=actorsAndSalaries
data
F=open('salaryData.pkl','wb')
pickle.dump(data, F)
F.close()
    
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