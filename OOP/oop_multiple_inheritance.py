class student:
     def __init__(self, name, batch, rollno):
         self.name=name
         self.batch=batch
         self.rollno=rollno

     def printdetails(self):
         return f"The name of student is {self.name}, batch is {self.batch}, and roll no is {self.rollno}"
    
class sportsman:
     no_of_games = 8
     def __init__(self, name, game):
         self.name=name
         self.game=game

     def printgame(self):
        return f"The name of sportsman is {self.name} and games played is {self.game}"

class coolstudent(student, sportsman):
     pass

Amaan= student("Amaan","IT",5)
Shaurya= sportsman("Shaurya",["cricket, badminton"])
Altamash= coolstudent("Altamash","CSE",28)

print(Amaan.printdetails())
print(Shaurya.printgame())
print(Altamash.printdetails())
print(Altamash.no_of_games)


# Altamash.game=["Cricket","Football"]
# print(Altamash.printgame())