#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:02:32 2019

@author: mackenziemitchell
"""

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

#getting HTML from fandago
response=requests.get('https://www.fandango.com/famous-actors-and-actresses')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
popCelebs=soup.findAll('div', {'class':'topperformers-row'})

#webscraping to create dictionary with rank and actor name
rankedCelebs=[]
for celeb in popCelebs:
    name = celeb.findAll('a')[1].text
    rankedCelebs.append(name)
actors = []
i=1
for celeb in rankedCelebs:
    actors.append({'name':celeb, 'rank':i})
    i+=1

#getting html from forbes
response=requests.get('https://www.forbes.com/sites/natalierobehmed/2017/08/22/full-list-the-worlds-highest-paid-actors-and-actresses-2017/#731b6e337515')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify

#webscraping to get actors and their salaires
actorSalaryData=soup.findAll('p')[7:37]
actorSalaryData[2].text
actorSalaryList=[]
for actor in actorSalaryData:
    actorSalaryList.append(actor.text)

#some preliminary analysis to see which actors are in both dictionaries
RichAndInfluencial=[]
for celeb in rankedCelebs:
    for actor in actorSalaryList:
        if celeb in actor:
            RichAndInfluencial.append(celeb)
