from ethan import *
class job:
    def __init__(self,memSize,pageCount,runTime):
            self.memSize=memSize
            self.pageCount=pageCount
            self.runTime=runTime
            self.timeRemaining=runTime
    def getMemSize(self):
        return self.memSize
    def getPageCount(self):
        return self.pageCount
    def getRunTime(self):
        return self.runTime
    def runJob(self,timeslice):
        self.timeRemaining=self.timeRemaining-timeslice
        if(self.timeRemaining<=0):
            self.timeRemaining=0
    def getTimeRemaining(self):
        return self.timeRemaining


def createJobs(memSize,pSize,jCount,maxRT,minRT,maxMem,minMem,seed):
    jobs[]
    return jobs