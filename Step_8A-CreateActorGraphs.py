#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:44:10 2019

@author: mackenziemitchell
"""

import db_funcs
import config
import json
import mysql
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline



with open('full_actor_list.json','r') as read_file:
    actorData= json.load(read_file)


actorData
cnx = mysql.connector .connect(
    host = config.host,
    user = 'mackenzie',
    passwd = config.password,
    database = 'movie_project'
)

import config
import importlib
importlib.reload(config)
conn = db_funcs.get_db_conn(config)

conn
c=conn.cursor()
c

def dynamic_entry_actors(actorList):
    cursor=conn.cursor()
    for actor in actorList:
        actor_id=actor['actor_id']
        first_name=actor['first']
        last_name=actor['last']
        pop_rank=actor['pop_rank']
        social_rank=actor['social']
        salary=actor['salary']
        db_funcs.insert_actor_values(cursor, actor_id, first_name, last_name, pop_rank, social_rank, salary)
        
dynamic_entry_actors(actorData)
conn.commit()
insert_str = """INSERT INTO moviesxactors (title_id, actor_id) VALUES (%s, %s) """
cursor.execute()
def insert_actors_movies(cursor, title_id, actor_id):
    insert_str = """INSERT INTO moviesxactors (title_id, actor_id) VALUES (%s, %s) """
    values = (title_id, actor_id)
    cursor.execute(insert_str, values)
import json

with open('cleaned_movie_data_for_50_actors.json','r') as read_file:
    movieData= json.load(read_file)
len(movieData)
movieData[0]

for movie in movieData:
    for member in movie['cast']:
        if member != None:
            if len(member)>30:
                member=None
movieData

c.execute("""select actor_id, first_name, last_name, pop_rank, avg(movies.bo_ww)
from actors
join moviesxactors
using (actor_id)
join movies
using (title_id)
group by actor_id
order by pop_rank""")

results0 = c.fetchall()

actor_names=[]
results0
for result in results0:
    name=result[1]+' '+result[2]
    actor_names.append(name)
actor_names

social_rank=[]


label=[]
for result in results0:
    rank=result[3]
    name=result[1]+' '+result[2]
    label.append({rank:name})
    
x0=[]
y=[]
for result in results0:
    x0.append(result[3])
    y.append(int(result[4]/1000000))
print(x0,y)
print(label)
# fig, ax = plt.subplots()
# ax.bar(x0,y, color='purple')



x = np.arange(len(results0))  # the label locations
print(x)
width = 0.5  # the width of the bars

fig, ax = plt.subplots(figsize=(100,60))
rects1 = ax.bar(x - width/2, y, width, label='Average Box Office Earnings/100,000', color='purple')

# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Box Office Earnings, in Millions')
ax.set_xlabel('Actors, Ranked By Popularity')
ax.set_title('Total Average Box Office Earnings Per Popular Actor')
ax.set_xticks(x)
ax.set_xticklabels(label, rotation = 50)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation= 0)

plt.rcParams.update({'font.size': 60})

autolabel(rects1)

# fig.tight_layout()
plt.savefig('BO_v_Pop.png')
plt.show()



c.execute("""select actor_id, first_name, last_name, salary, avg(movies.bo_ww)
from actors
join moviesxactors
using (actor_id)
join movies
using (title_id)
group by actor_id
order by salary""")

results1 = c.fetchall()

salaries=[]
for result in results1:
    if result[3]!=0:
        salaries.append(result)
salaries
labels2=[]
y1=[]
i=1
for salary in salaries[:-1]:
    y1.append(int(salary[4]/100000))
    labels2.append({salary[1]+' '+salary[2]:salary[3]})
    i+=1
print(y1)

print(labels2)

# fig, ax = plt.subplots()
# ax.bar(x1,y1,color='green')

x = np.arange(len(labels2))  # the label locations
width = 0.5  # the width of the bars

fig, ax = plt.subplots(figsize=(60,40))
rects1 = ax.bar(x - width/2, y1, width, label='Average Box Office Earnings/100,000', color='green')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Salaries of Actors in Millions')
ax.set_ylabel('Average Box Office Earnings')
ax.set_title('Avg B.O. Earnings Based on Total Salary Per Actor')
ax.set_xticks(x)
ax.set_xticklabels(labels2, rotation = 15)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation= 0)

plt.rcParams.update({'font.size': 50})

autolabel(rects1)

# fig.tight_layout()
plt.savefig('BO_v_Sal.png')
plt.show()

c.execute("""select actor_id, first_name, last_name, social_rank, avg(movies.bo_ww)
from actors
join moviesxactors
using (actor_id)
join movies
using (title_id)
where social_rank !=0
group by actor_id
order by social_rank""")

results2=c.fetchall()
results2

social=[]
for result in results:
    if result[3]!=0:
        social.append(result)
social

x2=[]
y2=[]
for s in results:
    x2.append(s[3])
    y2.append(int(s[4]/100000))
print(y2)
media=[]

for r in results:
    name=r[1]+' '+r[2]
    media.append(name)


def create_labels(list1):
    actor_names = []
    for i in range(len(list1)):
        actor_names.append({list1[i][1]+' '+list1[i][2]:list1[i][3]})
    return actor_names

actor_names=create_labels(results)

name=[]
for actor in actor_names:
    for k, v in actor.items():
        a=v
        name.append(a)
media

print(y2)
actor_names=create_labels(results)
actor_names

x = np.arange(len(actor_names))  # the label locations
width = 0.5  # the width of the bars

fig, ax = plt.subplots(figsize=(70,40))
rects1 = ax.bar(x - width/2, y2, width, label='Average Box Office Earnings/100,000', color='blue')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average B.O Earnings, in Millions')
ax.set_title('Actor Total Online Following')
ax.set_xticks(x)
ax.set_xticklabels(actor_names, rotation = 15)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation= 0)

plt.rcParams.update({'font.size': 50})

autolabel(rects1)

# fig.tight_layout()

plt.savefig('BO_v_Social.png')
plt.show()