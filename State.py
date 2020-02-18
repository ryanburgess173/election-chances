import random

class State:

    __finalElectoralVote = ""
    __rChance = 50
    __dChance = 50

    def __init__(self, name, party, electoralVotes, lean):
        self.__name = name
        self.__party =  party
        self.__electoralVotes = electoralVotes
        if(self.__party == 'R'):
            self.__rChance += lean
            self.__dChance -= lean
        else:
            self.__rChance -= lean
            self.__dChance += lean
        self.electionDay()

    def electionDay(self):
        vote = random.randint(1,100)
        if(self.__dChance > self.__rChance):
            if(vote <= self.__dChance):
                self.__finalElectoralVote = 'D'
            else:
                self.__finalElectoralVote = 'R'
        elif(self.__dChance <  self.__rChance):
            if(vote <= self.__rChance):
                self.__finalElectoralVote = 'R'
            else:
                self.__finalElectoralVote = 'D'
        else:
            self.__finalElectoralVote = 'T'

    def get_electoralVote(self):
        return self.__finalElectoralVote
