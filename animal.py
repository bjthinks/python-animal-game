import sys
import pickle

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
            tree.yesAnimal = playGame(tree.yesAnimal)
            return tree
        else:
            tree.noAnimal = playGame(tree.noAnimal)
            return tree
    elif isinstance(tree, Leaf):
        print("Is it a " + tree.animal + "?")
        answer = getYesNo()
        if answer:
            print("I got it!")
            return tree
        else:
            print("I guess I don\'t know enough about the " + tree.animal + ".")
            print("What was your animal?")
            userAnimal = input()
            print("Please type a yes-no question that would differentiate between")
            print("the " + tree.animal + " and the " + userAnimal + ".")
            print("Hint: this should be a question that can easily be answered \"yes\" or \"no\"")
            print("for any animal. Please include the question mark at the end of your question.")
            newQuestion = input()
            print("Would the answer to this question be yes or no for the")
            print(userAnimal + "?")
            if getYesNo():
                newBranch = Branch(newQuestion, Leaf(userAnimal), tree)
            else:
                newBranch = Branch(newQuestion, tree, Leaf(userAnimal))
            return newBranch
    else:
        print("UNKNOWN OBJECT IN DECISION TREE!")
        sys.exit(1)

try:
    with open("animal.dat", "rb") as brain:
        tree = pickle.load(brain)
        print("Loaded knowledge of animals from animal.dat")
except:
    tree = Leaf("bunny")

while True:
    print("Please think of a kind of animal. I will ask yes-no questions, and")
    print("try to guess what kind of animal you are thinking of.")
    tree = playGame(tree)
    print("Want to play again?")
    if not getYesNo():
        with open("animal.dat", "wb") as brain:
            pickle.dump(tree, brain)
            print("Saved what I know of animals to animal.dat")
        break
