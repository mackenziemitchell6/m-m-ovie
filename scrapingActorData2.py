#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:47:19 2019

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

rankedActors=[]
i=1
for celeb in actors:
    rankedActors.append({'name':celeb['name'].strip(), 'popularityRank':i})
    i+=1

rankedActors[1]['name']='Robert Downey'
rankedActors[26]['name']='Samuel Jackson'
rankedActors

data=rankedActors
data
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

for data in fbData:
    if data['name']=='Dwayne Johnson (The Rock)':
        data['name']='Dwayne Johnson'
    elif data['name']=='Eva Longoria Parker':
        data['name']='Eva Longoria'
    elif data['name']=='Jean-Claude Van Damme':
        data['name']='Jean Damme'
    elif data['name']=='Lee Minho (이민호)':
        data['name']='Lee Minho'
    elif data['name']=='Puss In Boots':
        data['name']='PussIn Boots'
    elif data['name']=='LL Cool J':
        data['name']='LL Cool'
    elif data['name']=='Robert De Niro':
        data['name']='Robert DeNiro'
    elif data['name']=='Melissa Joan Hart':
        data['name']='Melissa Hart'
    elif data['name']=='Helena Bonham Carter':
        data['name']='Helena Carter'
    elif data['name']=='Soleil Moon Frye':
        data['name']='Soleil Frye'
    elif data['name']=='Neil Patrick Harris':
        data['name']='Neil Harris'
    elif data['name']=='Shah Rukh Khan':
        data['name']='Shah Khan'
    elif data['name']=='Samuel L. Jackson':
        data['name']='Samuel Jackson'
    elif data['name']=='Roberto Gómez Bolaños (Chespirito)':
        data['name']='Roberto Bolanos'
    elif data['name']=='Fernanda Paes Leme':
        data['name']='Fernanda Leme'
    elif data['name']=='Michael Ian Black':
        data['name']='Michael Black'
for data in fbData:
    data['Online following']=int(re.sub(',',"",data['Online following']))
fbData
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
    actorsAndSalaries.append({'actorName':actorName.strip(),'salary':salary})

for actor in actorsAndSalaries:
    actor['actorName']=(actor['actorName'][:-1])
    actor['salary']=float(actor['salary'][:-8])
actorsAndSalaries[1]['actorName']='Dwayne Johnson'
actorsAndSalaries[5]['actorName']='Robert Downey'
actorsAndSalaries[7]['actorName']='Shah Khan'
actorsAndSalaries[12]['actorName']='Samuel Jackson'
actorsAndSalaries

actorHighSal=[]
for actor in actorsAndSalaries:
    actorHighSal.append(actor['actorName'])
actorsAndSalaries

data=actorsAndSalaries
data
F=open('salaryData.pkl','wb')
pickle.dump(data, F)
F.close()
    
RichAndInfluencial=[]
for line in fbData:
    for actor in actorHighSal:
        if line['name'] in actor:
            RichAndInfluencial.append(actor)
RichAndInfluencial

data=RichAndInfluencial
data
F=open('richSocialActors.pkl','wb')
pickle.dump(data, F)
F.close()

popAndRich=[]
for actor in popularActors:
    for celeb in actorHighSal:
        if actor in celeb:
            popAndRich.append(actor)
popAndRich

data=popAndRich
F=open('popularRichActors.pkl','wb')
pickle.dump(data, F)
F.close()

popAndInfluencial=[]
for actor in socialActorNames:
    for celeb in popularActors:
        if actor in celeb:
            popAndInfluencial.append(actor)
popAndInfluencial

data=popAndInfluencial
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

