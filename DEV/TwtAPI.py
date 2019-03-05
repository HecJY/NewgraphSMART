import twitter
import cPickle
import os
import difflib
import time

Datapath = os.path.expanduser('~DEV/graph/TweeterData')
def w_file1(api):
    path = os.path.join(Datapath,'twitter.txt')
    f = open(path, "w+")

    search = api.Getsearch('python')
    for x in search:
        f.write(cPickle.dumps(search))
    f.close()



def update(api):
    #update every five mins
    period = time.time() + 60*5
    while(time.time() < period)
    w_file(api)
    return


def data_cral():
    api = twitter.Api(consumer_key = 'x4FguSwehXpgdPtq2bTi5dOJU', consumer_secret = 'yAHfjLyxuct4I6He9uDbqr547MN0RP6ghdSFgYn19XDF4uXbge', access_token_key = '2219948304-c60sVwWulIqRJLnPSFH6rMWn9uMIvYxmQSTQx56', access_token_secret = 'dH11u0vsbWIiMBzgEbHTgpFSzlrmu0vhyGfqbXiRsBsUf')
    if not api.VerifyCredentials():
        raise TypeError("Verification failed")
    while(1):
        update(api)

    return

#Get the class in the file
def read_file():
    path = os.path.join(Datapath,'twitter.txt')
    f = open(path, "r")
    total_list = list()
    for line1 in f:
        user = cPickle.load(line1)
        total_list.append(user)

    return total_list
