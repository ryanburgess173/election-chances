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
            party = 'Republican'
            w = avgRepVote
            l = avgDemVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)
        elif(avgRepVote < avgDemVote):
            party = 'Democratic'
            w = avgDemVote
            l = avgRepVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)

        states.append(State(item['name'], party, item['electoralVotes'], lean))

    democraticStates = 0
    republicanStates = 0
    democraticReps = 0
    republicanReps = 0
    democraticVotes = 0
    republicanVotes = 0
    for state in states:
        print(state.get_stateName()+": "+state.get_party()+" lean of "+str(state.get_lean()) + "%")
        if(state.get_stateName() != "Washington D.C."):
            if(state.get_electoralVote()=='R'):
                republicanStates += 1
                republicanVotes+=state.getElectoralVotes()
                republicanReps += state.getElectoralVotes() - 2
            else:
                democraticStates += 1
                democraticReps += state.getElectoralVotes() - 2
                democraticVotes+=state.getElectoralVotes()
        else:
            if(state.get_electoralVote()=='R'):
                republicanVotes += state.getElectoralVotes()
            else:
                democraticVotes += state.getElectoralVotes()


main()
