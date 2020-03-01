
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

    memSize=int(argv[1])
    pSize=int(argv[2])
    jCount=int(argv[3])
    maxRT=int(argv[4])
    minRT=int(argv[5])
    maxMem=int(argv[6])
    minMem=int(argv[7])
    seed=int(argv[8])

    if(memSize%pSize!=0):
        print("Page Size is not multiple of Memory Size")
        return -1

    #would be useful to have a job class
    createJobs(memSize,pSize,jCount,maxRT,minRT,maxMem,minMem,seed)