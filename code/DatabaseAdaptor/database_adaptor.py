import pandas as pd

def connectDb():

    pass

def loadPreferences():
    database = pd.read_csv('database/Preferences.csv')
    return database

def loadThresholds():
    database = pd.read_csv('database/Thresholds.csv')
    return database


def loadProfessions():

    database = pd.read_csv('database/Professions.csv')
    return database
    
def loadTasks():

    database = pd.read_csv('database/Tasks.csv')
    return database

def loadActions():

    database = pd.read_csv('database/Actions.csv')
    return database



