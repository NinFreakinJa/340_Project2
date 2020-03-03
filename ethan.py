# ethan.py
# Ethan Guthrie
# 03/03/2020
# Provides the following class:
#   PageTable
# Provides the following methods:
#   doSimulation()
#   printJobInformation()

# Job class is required for job variables.
from reid import Job
# Math class is required for ceil() method.
from math import ceil

class PageTable:
    # Class initializer.
    def __init__(self, pageCount, pageSize):
        self.pageCount = pageCount
        self.pageSize = pageSize
        self.pages = []
        for i in range(0, pageCount):
            self.pages.append(".")

    # Class methods.
    def addJob(self, id, memSize):
        pageRequirement = ceil(memSize/self.pageSize)
        if not addJobHelp(pageRequirement):
            return False
    def addJobHelp(self, pageRequirement):
        counter = 0
        for page in self.pages:
            if page == ".":
                counter += 1
        return counter >= pageRequirement
    def printTable(self):
        for i in range(0, len(self.pages)):
            if i == 0 or i % 4 != 0:
                print(self.pages[i], end="")
            elif i % 16 == 0:
                print("\n" + self.pages[i], end="")
            else:
                print(" " + self.pages[i], end="")
        print()
  
# Runs the simulation.
def doSimulation():
    pass

# Prints job information.
def printJobInformation():
    pass

test = PageTable(48, 130)
test.printTable()