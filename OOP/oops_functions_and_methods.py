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
    

amaan = Student("Amaan",10, 5)
Shaurya = Student("Shaurya",9, 20)
# print(amaan.name)
# print(amaan.no_of_subjects)
# amaan.change_subjects(8)
# print(amaan.no_of_subjects)
# print(Shaurya.no_of_subjects)
# print(amaan.printdetails())
# hasnain=Student.from_dash("Hasnain-11-28")
# print(hasnain.name)

amaan.good(" Amaan")
