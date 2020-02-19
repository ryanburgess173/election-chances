import random

class State:

    __finalElectoralVote = ""
    __rChance = 50
    __dChance = 50
    __margin = 0

    def __init__(self, name, party, electoralVotes, lean):
        self.__name = name
        self.__party =  party
        self.__electoralVotes = electoralVotes
        self.__lean = lean
        if(self.__party == 'R'):
            self.__rChance += (lean)
            self.__dChance -= (lean)
        else:
            self.__rChance -= (lean)
            self.__dChance += (lean)
        self.electionDay()

    def electionDay(self):
        vote = random.randint(1,100)
        if(self.__dChance > self.__rChance):
            if(vote <= self.__dChance):
                self.__finalElectoralVote = 'D'
            else:
                self.__finalElectoralVote = 'R'
            self.__margin = abs(self.__dChance - vote)
        elif(self.__dChance <  self.__rChance):
            if(vote <= self.__rChance):
                self.__finalElectoralVote = 'R'
            else:
                self.__finalElectoralVote = 'D'
            self.__margin = abs(self.__rChance - vote)
        else:
            tiebreaker = random.randint(1,100)
            if(tiebreaker<51):
                self.__finalElectoralVote = 'D'
                self.__margin = abs(50-tiebreaker)
            else:
                self.__finalElectoralVote = 'R'
                self.__margin = abs(50-tiebreaker)

    def get_electoralVote(self):
        return self.__finalElectoralVote

    def get_stateName(self):
        return self.__name

    def get_margin(self):
        return self.__margin

    def getElectoralVotes(self):
        return self.__electoralVotes

    def get_party(self):
        return self.__party

    def get_lean(self):
        return self.__lean
