class A:
    anumber = 45
    def __init__(self,name,rollno,mark,work):
        self.name= name
        self.rollno= rollno
        self.mark= mark
        self.work= work
    
    def printdetails(self):
        return f"Name - {self.name}, Rollno - {self.rollno}, Work - {self.work}"
    
    def __add__(self, other):
        return self.mark + other.mark
    def __repr__(self):
        return f"{self.name} ({self.rollno},{self.mark},'{self.work}')"   
    def __str__(self):
        return f"Name - {self.name}, Rollno - {self.rollno}, Work - {self.work}"

ramesh=A("Ramesh",5,87,"Graphic designer")
suresh=A("suresh",12,94,"Web Devoloper")

# first preference is of __str__ 
# if __str__ doesn't exist then it prints __repr__
print(ramesh) 
# to call repr
print(repr(ramesh)) 
# to call str
print(str(ramesh)) 
