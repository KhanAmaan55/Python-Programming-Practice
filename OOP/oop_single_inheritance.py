class Student():
    """
    student class for practice
    """
    no_of_subjects=10
    def __init__ (self,name, std, rollno):
        """
        init function to initialize the values
        """
        self.name= name
        self.std= std
        self.rollno= rollno
    def printdetails(self):
        """
        print details
        """
        return f"The name is {self.name},The rollno is {self.rollno},The standard is {self.std}"
    @classmethod
    def change_subjects(cls, new):
        cls.no_of_subjects=new
    
    @classmethod
    def from_dash(cls, string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    @staticmethod
    def good(string):
        print("This is good"+string)
    
class programmar(Student):
    # # We can make another init function or we can use the existing one
    # # we can do it with the help of super().__init__
    def __init__(self, name, std ,rollno, language ):
        self.name=name
        self.std=std
        self.rollno=rollno
        self.language=language
    def printprog(self):
        return f"The name is {self.name},The rollno is {self.rollno},The standard is {self.std}, Languages known {self.language}"
    
amaan = Student("Amaan",10, 5)
Shaurya = Student("Shaurya",9, 20)

altamash= programmar("Altamash", 20, 7,["Python","c++"])
print(altamash.printprog())