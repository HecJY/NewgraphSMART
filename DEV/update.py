import stream
from twython import TwythonStreamer,Twython
import csv
import os
import sys
import twython
from pprint import pprint as pp
import time

class TwythonListener(Twython):
    

#Create a tweet stream listener

    #this function has to check the differences in the existed files, if any changes, the change has to be taken care of

    #might be able to use some other libraries to do
