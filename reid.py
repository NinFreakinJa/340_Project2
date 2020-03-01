from ethan import *
import random
#A class for holding information on a job
class Job:
    def __init__(self,memSize,runTime):
            self.memSize=memSize
            self.pageCount=0
            self.runTime=runTime
            self.timeRemaining=runTime
            self.complete=False
    def getMemSize(self):
        return self.memSize
    def getPageCount(self):
        return self.pageCount
    def setPageCount(self,count):
        self.pageCount=count
    def getRunTime(self):
        return self.runTime
    def runJob(self,timeslice):
        self.timeRemaining=self.timeRemaining-timeslice
        if(self.timeRemaining<=0):
            self.timeRemaining=0
            self.complete=True
    def getTimeRemaining(self):
        return self.timeRemaining
    def isComplete(self):
        return self.complete

#Creates a list of jobs with given parameters
def createJobs(jCount,maxRT,minRT,maxMem,minMem,seed):
    random.seed(seed)
    jobs=[]
    for i in range(0,jCount):
        jMemSize=random.randint(minMem,maxMem)
        jRunTime=random.randint(minRT,maxRT)
        newJob=Job(jMemSize,jRunTime)
        jobs.append(newJob)
    return jobs

def printParameters(memSize,pSize,jCount,maxRT,minRT,maxMem,minMem,seed):
    print("Simulator Parameters:")
    print("Memory Size:"+str(memSize))
    print("Page Size:"+str(pSize))
    print("Random Seed:"+str(seed))
    print("Number of Jobs:"+str(jCount))
    print("Runtime (min-max) timesteps:"+str(minRT)+"-"+str(maxRT))
    print("Memory (min-max):"+str(minMem)+"-"+str(maxMem))

def printJobQueue(jobs):
    print("Job Queue:")
    print("Job #    Runtime    Memory")
    for i in range(0,len(jobs)):
        print((" "*(5-len(str(i))))+str(i)+(" "*(11-len(str(jobs[i].getRunTime))))+str(jobs[i].getRunTime)+(" "*(10-len(str(jobs[i].getMemSize))))+str(jobs[i].getMemSize))