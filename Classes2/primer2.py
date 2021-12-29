class Chef: #
    def _beshbarmak(self): #
        return 'Бешбармак' #

    def __shorpo(self): #
        return 'Шорпо' #


class Trainee(Chef): #
    def borsh(self): #
        return 'Борщ' #


class TraineeTwo(Trainee): #
    pass #


azamat = Chef() #
print(azamat._Chef__shorpo()) #

nurlan = Trainee() #
print(nurlan._Chef__shorpo()) #

marat = TraineeTwo() #
print(marat._Chef__shorpo()) #