class Branch(object):
    def __init__(self, question_, yesAnimal_, noAnimal_):
        self.question = question_
        self.yesAnimal = yesAnimal_
        self.noAnimal = noAnimal_

class Leaf(object):
    def __init__(self, animal_):
        self.animal = animal_

def getYesNo():
    str = input()
    if str == "yes":
        return True;
    elif str == "no":
        return False;
    else:
        print("Please enter yes or no!")
        return getYesNo();

def playGame(tree):
    if isinstance(tree, Branch):
        print(tree.question)
        if getYesNo():
            playGame(tree.yesAnimal)
        else:
            playGame(tree.noAnimal)
    elif isinstance(tree, Leaf):
        print("Is it a " + tree.animal + "?")
        answer = getYesNo()
        if answer:
            print("I got it!")
            return
        else:
            print("I guess I don\'t know enough about the " + tree.animal + ".")
            return
    else:
        print("UNKNOWN OBJECT IN DECISION TREE!")

tree = Leaf("bunny")

print("Please think of a kind of animal. I will ask yes-no questions, and")
print("try to guess what kind of animal you are thinking of.")

playGame(tree)
