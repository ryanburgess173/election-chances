import json
from State import State

def readData():

    states = {}

    data = json.load(open('electionData.json'))

    for item in data['states']:
        states[item['name']] = State(
            item['name'],
            item['party'],
            item['electoralVotes'],
            item['lean']
        )

    print(states)
    
readData()
