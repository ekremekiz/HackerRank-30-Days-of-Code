class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
	# Add your code here

    def computeDifference(self):
        temp = 0
        for i in self.__elements:
            for j in self.__elements:
                temp = abs(i-j)
                if temp>self.maximumDifference:
                    self.maximumDifference = temp
    
    def maximumDifference(self):
        return self.maximumDifference
            
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)