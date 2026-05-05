class Node(object):
    def __init__(self, question_, yesAnimal_, noAnimal_):
        self.question = question_
        self.yesAnimal = yesAnimal_
        self.noAnimal = noAnimal_

class Leaf(object):
    def __init__(self, animal_):
        self.animal = animal_

def playGame(tree):
    if isinstance(tree, Leaf):
        print("Is it a " + tree.animal + "?")
        answer = input()
        if answer == "yes":
            print("I got it!")
            return
        elif answer == "no":
            print("I guess I don\'t know enough about the " + tree.animal + ".")
            return
        else:
            print("SYNTAX ERROR")
            exit()

tree = Leaf("bunny")

print("Please think of a kind of animal. I will ask yes-no questions, and")
print("try to guess what kind of animal you are thinking of.")

playGame(tree)
