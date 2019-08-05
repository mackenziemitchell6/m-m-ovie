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
import time

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
    actors.append({'name':celeb, 'rank':i})
    i+=1

response=requests.get('https://www.forbes.com/sites/natalierobehmed/2017/08/22/full-list-the-worlds-highest-paid-actors-and-actresses-2017/#731b6e337515')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
actorSalaryData=soup.findAll('p')[7:37]
actorSalaryData[2].text
actorSalaryList=[]
for actor in actorSalaryData:
    actorSalaryList.append(actor.text)

RichAndInfluencial=[]
for celeb in rankedCelebs:
    for actor in actorSalaryList:
        if celeb in actor:
            RichAndInfluencial.append(celeb)
