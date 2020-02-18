import json
import math
from State import State

def readData():

    states = []

    data = json.load(open('electionData.json'))

    for item in data['states']:
        print("\n--------------------")
        print(item['name'])
        print("--------------------")
        avgRepVote = (item['r2016Votes']+item['r2012Votes'] +
                      item['r2008Votes']+item['r2004Votes'])/4
        print("Average Republican Vote:", avgRepVote)
        avgDemVote = (item['d2016Votes']+item['d2012Votes'] +
                      item['d2008Votes']+item['d2004Votes'])/4
        print("Average Democratic Vote:", avgDemVote)
        if(avgRepVote > avgDemVote):
            party = 'R'
            w = avgRepVote
            l = avgDemVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)
            print(lean, "lean Republican")
        elif(avgRepVote < avgDemVote):
            party = 'D'
            w = avgDemVote
            l = avgRepVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)
        
        states.append(State(item['name'], party, item['electoralVotes'], lean))
    
readData()
