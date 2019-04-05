import pandas as pd
from pprint import pprint as pp
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import stream
import plotly.plotly as py
import plotly.graph_objs as go

import networkx as nx


def readfile():
    data = pd.read_csv("saved_tweets.csv",header=None)
    likes = data[data.columns[0]]
    user = data[data.columns[1]]
    retweets= data[data.columns[2]]
    return data


#update the x, y coordinates as x is corresponding to likes, y is corresponding to number of retweets
def filter(likes, user, retweets):
    userinfo = list()
    filterdic = dict()
    x = 0
    while x < len(likes):
        if (int(likes[x])+int(retweets[x])) >= 1000:
            userinfo=list()
            xcor = int(likes[x])/1000
            ycor = int(retweets[x])/1000
            popul = xcor+ycor
            userinfo.append(xcor)
            userinfo.append(ycor)
            userinfo.append(popul)
            filterdic[user[x]] = userinfo
        x +=1
    sum = 0
    for a in filterdic:
        sum+=filterdic[a][1]+filterdic[a][0]

    for b in filterdic:
        populrate = (filterdic[b][0]+filterdic[b][1])/sum
        filterdic[b].append(populrate)


    return filterdic

def display(userinfo:dict):

    for name in userinfo:
        x = userinfo[name][0]
        y = userinfo[name][1]
        plt.scatter(x, y, s=(userinfo[name][2]*100), alpha=0.5)
    plt.show()



if __name__ == "__main__":
    data = readfile()
    likes=list(data[data.columns[0]])
    user=list(data[data.columns[1]])
    retweets=list(data[data.columns[2]])

    filtered = filter(likes,user, retweets)
    pp(filtered)
    display(filtered)
