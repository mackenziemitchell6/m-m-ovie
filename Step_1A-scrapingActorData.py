#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:47:19 2019

@author: mackenziemitchell
"""
#importing libaries that may be needed
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import pickle

#getting html from Fandago
response=requests.get('https://www.fandango.com/famous-actors-and-actresses')
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify
#beginning to scrape
popCelebs=soup.findAll('div', {'class':'topperformers-row'})

#appending the actor data to a list of popular actor names
rankedCelebs=[]
for celeb in popCelebs:
    name = celeb.findAll('a')[1].text
    rankedCelebs.append(name)
actors = []
i=1
#appending actor name and rank to a list of dictionaries of popular actors
for celeb in rankedCelebs:
    actors.append({'name':celeb, 'popularityRank':i})
    i+=1
actors

#Cleaning up popular actor data
rankedActors=[]
i=1
for celeb in actors:
    rankedActors.append({'name':celeb['name'].strip(), 'popularityRank':i})
    i+=1
    
#These actors had 3 names, not 2 like the rest of the data
rankedActors[1]['name']='Robert Downey'
rankedActors[26]['name']='Samuel Jackson'
rankedActors

#storing cleaned popular actor data in a pickle file
data=rankedActors
data
F=open('popularActorsRanked.pkl','wb')
pickle.dump(data, F)
F.close()

onlinePres=[]
fbData=[]
socialActorNames=[]
#Must create a list of all page numbers that we want to scrape
pagenum=['1','2','3','4','5','6','7','8','9','10']
for page in pagenum:
    #getting html for fanpagelist for each page
    response=requests.get('https://fanpagelist.com/category/actors/view/list/sort/fans/page'+page)
    soup=BeautifulSoup(response.content,'html.parser')
    soup.prettify
    #scraping the webpage, page by page and appending the actor name to a list
    facebookActors=soup.findAll('span',{'class':"title"})
    totalOnlinePres=soup.findAll('div',{'class':'total_stats'})
    for actor in totalOnlinePres:
        onlinePres.append(actor.text)
    i=0
    #scraping the webpage again, but this time appending the actor name and their online following to a list of dictionaries
    for actor in facebookActors[0:20]:
        fbData.append({'name':actor.text,"Online following":onlinePres[i]})
        i+=1
#cleaning up the list of popular actor names
    for actor in facebookActors[0:20]:
        socialActorNames.append(actor.text)

#changing all actors who have 3 or more names to our standard one name
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
        #more cleaning to remove commas
for data in fbData:
    data['Online following']=int(re.sub(',',"",data['Online following']))
fbData
#storing in a pickle file
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
#creating a list for just the names of highly paid actors
for actor in actorSalaryData:
    actorSalaryList.append(actor.text)
actorsAndSalaries=[]

#creating a list AND cleaning the data a little, had to cut each element of the list at the '$' to get name AND salary
actorSalaryList
for actor in actorSalaryList:
    actorName, salary = actor[3:].split('$')
    actorsAndSalaries.append({'actorName':actorName.strip(),'salary':salary})

#cleaning data more, standardizing names to only have 2 names
for actor in actorsAndSalaries:
    actor['actorName']=(actor['actorName'][:-1])
    actor['salary']=float(actor['salary'][:-8])
actorsAndSalaries[1]['actorName']='Dwayne Johnson'
actorsAndSalaries[5]['actorName']='Robert Downey'
actorsAndSalaries[7]['actorName']='Shah Khan'
actorsAndSalaries[12]['actorName']='Samuel Jackson'
actorsAndSalaries
#cleaning list of highly paid actors names
actorHighSal=[]
for actor in actorsAndSalaries:
    actorHighSal.append(actor['actorName'])
actorsAndSalaries
#storing in a pickle file
data=actorsAndSalaries
data
F=open('salaryData.pkl','wb')
pickle.dump(data, F)
F.close()
    
    
#The rest of the code is simply preliminary cross-referencing to get an idea of which actors are on more than one list
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

