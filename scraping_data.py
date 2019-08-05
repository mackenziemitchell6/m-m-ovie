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
    actors.append({'name':celeb, 'popularityRank':i})
    i+=1
actors

popactorNames=[]
for celeb in rankedCelebs:
    popactorNames.append(celeb)
popactorNames

response=requests.get('https://www.ranker.com/list/100-powerful-celebrities-with-highest-social-site-ranking/worlds-richest-people-lists')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
powCelebs=soup.findAll('div', {'class':'listItem__data'})
powCelebs
social=[]

for celeb in powCelebs:
    if len(celeb) > 0:
        newpow=celeb.findAll('a',{'class':'listItem__title listItem__title--link black'})
        social.extend(newpow)

social
social1=[]
for soc in social:
    social1.append(soc.text)
    
social1

response=requests.get('https://www.forbes.com/sites/natalierobehmed/2017/08/22/full-list-the-worlds-highest-paid-actors-and-actresses-2017/#731b6e337515')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
actorSalaryData=soup.findAll('p')[7:37]
actorSalaryData[2].text
actorSalaryList=[]
for actor in actorSalaryData:
    actorSalaryList.append(actor.text)
actorSalaryList

response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page1')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
fbData=[]
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1

socialActorNames=[]
for actor in facebookActors:
    socialActorNames.append(actor.text)

response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page2')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1
for actor in facebookActors:
    socialActorNames.append(actor.text)

response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page3')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1
    
for actor in facebookActors:
    socialActorNames.append(actor.text)
    
response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page4')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1

for actor in facebookActors:
    socialActorNames.append(actor.text)
    
response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page5')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1
    
for actor in facebookActors:
    socialActorNames.append(actor.text)
    
response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page6')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1

for actor in facebookActors:
    socialActorNames.append(actor.text)
    
response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page7')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1
    
for actor in facebookActors:
    socialActorNames.append(actor.text)
    
response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page8')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1
    
for actor in facebookActors:
    socialActorNames.append(actor.text)
    
response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page9')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1
    
for actor in facebookActors:
    socialActorNames.append(actor.text)

response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page10')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
facebookActors=soup.findAll('span',{'class':"title"})
totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
onlinePres=[]
for actor in totalOnlinePres:
    onlinePres.append(actor.text)
i=0
for actor in facebookActors[0:20]:
    fbData.append({'name':actor.text,"Online following":onlinePres[i]})
    i+=1

for actor in facebookActors:
    socialActorNames.append(actor.text)
socialActorNames

response=requests.get('https://www.forbes.com/sites/natalierobehmed/2017/08/22/full-list-the-worlds-highest-paid-actors-and-actresses-2017/#731b6e337515')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
actorSalaryData=soup.findAll('p')[7:37]
actorSalaryData[2].text
actorSalaryList=[]
for actor in actorSalaryData:
    actorSalaryList.append(actor.text)
actorSalaryList
actorSalaryList

RichAndInfluencial=[]
for celeb in socialActorNames:
    for actor in actorSalaryList:
        if celeb in actor:
            RichAndInfluencial.append(celeb)
RichAndInfluencial

popAndRich=[]
for actor in popactorNames:
    for celeb in actorSalaryList:
        if actor in celeb:
            popAndRich.append(actor)
popAndRich

popAndInfluencial=[]
for actor in socialActorNames:
    for celeb in popactorNames:
        if actor in celeb:
            popAndInfluencial.append(actor)
popAndInfluencial

popInfluRich=[]
for actor in popAndInfluencial:
    for celeb in popAndRich:
        if actor in celeb:
            popInfluRich.append(actor)
popInfluRich
