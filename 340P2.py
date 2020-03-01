
# Libraries named after authors of this assignment contain methods written
# by the author after whom the file was named.
from ethan import *
from reid import *
# The sys library allows for python to access command-line arguments.
from sys import argv

def main():
    if len(argv) !=9:
        print("Usage:python3 340P2.py memorySize pageSize jobCount maxRunTime minRunTime maxMemory minMemory randomSeed")
        return -1

        #he didn't specify what to do for the time slice

        #how would you do the example he gives with set RANDOMSEED=n13

    int memSize=argv[1]
    int pSize=argv[2]
    int jCount=argv[3]
    int maxRT=argv[4]
    int minRT=argv[5]
    int maxMem=argv[6]
    int minMem=argv[7]
    int seed=argv[8]

    #would be useful to have a job class
    createJobs(memSize,pSize,jCount,maxRT,minRT,maxMem,minMem,seed)