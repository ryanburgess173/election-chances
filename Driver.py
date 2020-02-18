from State import State

def main():

    dCount = 0
    rCount = 0
    for i in range(1,1000):
        vote = State("Washington", 'D', 8, 4).get_electoralVote()
        if(vote == 'D'):
            dCount +=1
        else:
            rCount +=1

    print("R:",rCount)
    print("D:",dCount)

main()
