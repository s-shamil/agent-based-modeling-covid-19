from Persons.Person import Person
from Persons.PersonManager import PersonManager
from Tasks.Task import Task
from Tasks.TaskManager import TaskManager
from Actions.Action import Action
from Actions.ActionManager import ActionManager
from Simulator.Simulator import Simulator
from DatabaseAdaptor.database_adaptor import loadPreferences, loadTasks, loadActions, loadProfessions, loadThresholds
from Random.string_generator import rands
from Random.normal_distribution import randni
import numpy as np
import random




def main():
    fline = open("seed.txt").readline().rstrip()
    ranseed = int(fline)
    np.random.seed(ranseed)
    random.seed(ranseed)

    preferences_df = loadPreferences()
    thresholds_df = loadThresholds()
    profession_df = loadProfessions()
    actions_df = loadActions()
    tasks_df = loadTasks()

    trace_days = 2
    tracing_percentage = 0.3
    smartphone_owner_percentage = 0.75
    quarantine_days = 14


    timerun = 0 #0 if we want snapshots, any other value if we don'tc
    beginmodel = 1 #the day from which we want the simulation to start
    snapdays = [10, 14, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120] #the days we want the snapshots of (index always from original day 1)
    #outfile = open("Outputarray.txt","w+")
    #outfile.write(str(snapdays))
    Simulator.start_simulation(trace_days, tracing_percentage, smartphone_owner_percentage, quarantine_days, preferences_df, profession_df, actions_df, tasks_df, thresholds_df,timerun,snapdays, beginmodel)

    

    
    

if __name__ == '__main__':

    main()

