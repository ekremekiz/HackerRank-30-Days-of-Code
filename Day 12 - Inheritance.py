class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
                   
    def calculate(self):
        
        sumScores = 0
        for i in self.scores:
            sumScores += int(i)
        scores = sumScores / len(self.scores)
        
        if scores >= 90 and scores <= 100:
            grade = "O"
        elif scores >= 80 and scores < 90:
            grade = "E"
        elif scores >= 70 and scores < 80:
            grade = "A"
        elif scores >= 55 and scores < 70:
            grade = "P"
        elif scores >= 40 and scores < 55:
            grade = "D"
        else:
            grade = "T"
        return grade
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())