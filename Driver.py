import json
import math
from State import State


def main():

    states = []

    data = json.load(open('electionData.json'))

    for item in data['states']:
        avgRepVote = (item['r2016Votes']+item['r2012Votes'] +
                      item['r2008Votes']+item['r2004Votes'])/4
        avgDemVote = (item['d2016Votes']+item['d2012Votes'] +
                      item['d2008Votes']+item['d2004Votes'])/4
        if(avgRepVote > avgDemVote):
            party = 'R'
            w = avgRepVote
            l = avgDemVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)
        elif(avgRepVote < avgDemVote):
            party = 'D'
            w = avgDemVote
            l = avgRepVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)

        states.append(State(item['name'], party, item['electoralVotes'], lean))

    for state in states:
        input("Next State...")
        print(state.get_stateName())
        print(state.get_electoralVote())
        print(state.get_margin())

main()
