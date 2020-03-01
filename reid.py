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
    return jobs
