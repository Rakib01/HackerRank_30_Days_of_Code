class Difference:
    def __init__(self, a):
        self.__elements = a

        # Add your code here

    def __init__(self, a):

        self.__elements = a

        self.maximumDifference = 0

    def computeDifference(self):

        x = 101

        y = 0

        for item in self.__elements:

            if item < x:

                x = item

            if item > y:

                y = item

        self.maximumDifference = y - x
# End of Difference class
