# ethan.py
# Ethan Guthrie
# 03/03/2020
# Provides the following class:
#   PageTable
# Provides the following methods:
#   doSimulation()
#   doSimulationHelp()
#   printJobInformation()

# Job class is required for job variables.
from reid import Job
# Math class is required for ceil() method.
from math import ceil

# TODO: REMOVE SLEEP
from time import sleep

class PageTable:
    # Class initializer.
    def __init__(self, pageCount, pageSize):
        self.pageCount = pageCount
        self.pageSize = pageSize
        self.pages = []
        for i in range(0, pageCount):
            self.pages.append(".")

    # Class methods.
    def addJob(self, jobID, memSize):
        pageRequirement = ceil(memSize/self.pageSize)
        if not self.addJobHelp(pageRequirement):
            return False
        for i in range(0, len(self.pages)):        
            if self.pages[i] == ".":
                self.pages[i] = str(jobID)+" "
                pageRequirement -= 1
            if pageRequirement == 0:
                return True
    def addJobHelp(self, pageRequirement):
        counter = 0
        for page in self.pages:
            if page == ".":
                counter += 1
        return counter >= pageRequirement
    def clearJob(self, jobID):
        for i in range(0, len(self.pages)):        
            if self.pages[i] == str(jobID)+" ":
                self.pages[i] = "."
    def printTable(self):
        for i in range(0, len(self.pages)):
            if i == 0:
                print("       " + self.pages[i], end="")
            elif i % 4 != 0:
                print(self.pages[i], end="")
            elif i % 16 == 0:
                print("\n       " + self.pages[i], end="")
            else:
                print(" " + self.pages[i], end="")
        print()
  
# Runs the simulation.
def doSimulation(jobs, pageCount, pageSize, timeSlice=1):
    print("Simulator Starting:\n")
    # Initializing simulator variables.
    pt = PageTable(pageCount, pageSize)
    counter = 1
    timeCounter = 1

    # Initializing simulation.
    for job in jobs:
        if pt.addJob(job.getJobID(), job.getMemSize()):
            print("Job " + str(job.getJobID()) + " Starting")
            job.setStatus("STOPPED")
        else:
            print("Job " + str(job.getJobID()) + " Waiting")
    for job in jobs:
        if job.getStatus() == "STOPPED":
            job.setStatus("RUNNING")
            break

    while doSimulationHelp(jobs):
        # Initializing current pass by starting first stopped process and incrementing time.
        timeCounter += 1
        for job in jobs:
            if job.getStatus() == "STOPPED":
                job.setStatus("RUNNING")

        # Letting each running job run for one time slice (size 1).
        nextJob = False
        for job in jobs:
            if job.getStatus() == "WAITING":
                if pt.addJob(job.getJobID(), job.getMemSize()):
                    print("Job " + str(job.getJobID()) + " Starting")
                    job.setStatus("STOPPED")
            if job.getStatus() == "STOPPED" and nextJob:
                job.setStatus("RUNNING")
                nextJob = False
                break
            elif job.getStatus() == "RUNNING":
                job.setStatus("STOPPED")
                nextJob = True
                print("Job " + str(job.getJobID()) + " Running")
                job.runJob(timeSlice)
                if job.getStatus() == "COMPLETE":
                    print("Job " + str(job.getJobID()) + " Completed")
                    pt.clearJob(job.getJobID())
                    job.setEndTime(timeCounter)
                pt.printTable()
                print()

# Helps with the simulation.
def doSimulationHelp(jobs):
    for job in jobs:
        if job.getStatus() != "COMPLETE":
            return True
    return False

# Prints job information.
def printJobInformation(jobs):
    print("Job Information:\n\n   Job #   Arrival Time   End Time")
    for job in jobs:
        jobNum = " " * (8 - len(str(job.getJobID()))) + str(job.getJobID())
        jobArrivalTime = " " * (15 - len(str(job.getRunTime()))) + str(job.getArrivalTime())
        jobEndTime = " " * (11 - len(str(job.getEndTime()))) + str(job.getEndTime())
        print(jobNum + jobArrivalTime + jobEndTime)