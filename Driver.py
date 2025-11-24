import json
import math
from State import State


def calculate_states(data, year=None):
    states = []
    
    for item in data['states']:
        if year:
            # Calculate for specific year
            repVote = item[f'r{year}Votes']
            demVote = item[f'd{year}Votes']
        else:
            # Calculate average across all years
            avgRepVote = (item['r2024Votes']+item['r2020Votes']+item['r2016Votes']+item['r2012Votes'] +
                          item['r2008Votes']+item['r2004Votes'])/6
            avgDemVote = (item['d2024Votes']+item['d2020Votes']+item['d2016Votes']+item['d2012Votes'] +
                          item['d2008Votes']+item['d2004Votes'])/6
            repVote = avgRepVote
            demVote = avgDemVote
            
        if(repVote > demVote):
            party = 'Republican'
            w = repVote
            l = demVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)
        elif(repVote < demVote):
            party = 'Democratic'
            w = demVote
            l = repVote
            lean = int(math.ceil((100*(w/(w+l))) - abs(100*(l/(w+l))))/2)

        states.append(State(item['name'], party, item['electoralVotes'], lean))
    
    return states


def display_results(states, title):
    print("\n" + "="*60)
    print(title)
    print("="*60)
    
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
    
    print("\n" + "-"*60)
    print(f"Democratic Electoral Votes: {democraticVotes}")
    print(f"Republican Electoral Votes: {republicanVotes}")
    print("-"*60)


def main():
    data = json.load(open('electionData.json'))
    
    # Show average from 2004-2024
    states_avg = calculate_states(data)
    display_results(states_avg, "Average Lean (2004-2024)")
    
    # Allow user to query specific years
    while True:
        print("\nEnter a year to see results for that specific election")
        print("Valid years: 2004, 2008, 2012, 2016, 2020, 2024")
        print("Or enter 'quit' to exit")
        
        user_input = input("\nYear: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        if user_input in ['2004', '2008', '2012', '2016', '2020', '2024']:
            states_year = calculate_states(data, user_input)
            display_results(states_year, f"{user_input} Election Results")
        else:
            print("Invalid year. Please enter 2004, 2008, 2012, 2016, 2020, or 2024")


main()
