from Tasks.TaskManager import TaskManager
from DatabaseAdaptor.utils import dfToFloat, dfToInt
import numpy as np
import pickle

class DaySimulator:

    def __init__(self):

        pass


    @staticmethod
    def generateDailyTasks(persons, tasks_df, lockdown_started, print_opt=False):

        for prsn in persons:
            prof_pers = prsn.profession
            if str(prof_pers) == "Unemployed":
                prob = np.random.rand()
                #70% unemployed does not get out if lockdown started 
                if (lockdown_started and prob < 0.7):
                    prsn.setTasks(TaskManager.generateTasks(tasks_df[tasks_df["profession"]=="NoOutingAllowed"]))
                else:
                    prsn.setTasks(TaskManager.generateTasks(tasks_df[tasks_df["profession"]=="Unemployed"]))
                
            elif str(prof_pers) == "Doctor":
                prsn.setTasks(TaskManager.generateTasks(tasks_df[tasks_df["profession"]=="Doctor"]))
            elif str(prof_pers) == "Student":
                prsn.setTasks(TaskManager.generateTasks(tasks_df[tasks_df["profession"]=="Student"]))
            elif str(prof_pers) == "Service":
                prsn.setTasks(TaskManager.generateTasks(tasks_df[tasks_df["profession"]=="Service"]))
            else:
                #isolated- no task - empty list
                prsn.setTasks([])

            if(print_opt):
                print('=== {} ==='.format(prsn.profession))
                TaskManager.printTasks(prsn.tasks)

    @staticmethod
    def dayStart(persons, day_cnt, preferences_df):

        # fline = open("seed.txt").readline().rstrip()
        # ranseed = int(fline)
        # np.random.seed(ranseed)
        awareness_start = dfToInt(preferences_df,"awareness_start")
        quarantine_start = dfToInt(preferences_df,"quarantine_start")
        

        for prsn in persons:
            
            prsn.infection_level = 0.0

            if(day_cnt>=awareness_start):

                prsn.raiseAwareness()

                prsn.becomeProtected()


        
        service_holder_cnt = 0
        service_holders = []

        stdnt_cnt = 0

        stdnts = []

        quarantined_person_ratio = dfToFloat(preferences_df,"quarantined_person_ratio")

        if(day_cnt==quarantine_start):
            print("Quarantine Starts today. Day -> "+ str(day_cnt))
            for prsn in persons:

                if(prsn.profession=='Service'):

                    service_holder_cnt += 1

                    service_holders.append(prsn.id)
                elif(prsn.profession=='Student'):
                    stdnt_cnt += 1

                    stdnts.append(prsn.id)

        
        quarantined_person_cnt = int(service_holder_cnt*quarantined_person_ratio)

        np.random.shuffle(service_holders)


        for i in range(quarantined_person_cnt):

            persons[service_holders[i]].profession = "Unemployed"

        for i in range(stdnt_cnt):

            persons[stdnts[i]].profession = "Unemployed"

                


    @staticmethod
    def dayEnd(persons, thresholds_df, num_of_day, trace_days, quarantine_days):
        # fline = open("seed.txt").readline().rstrip()
        # ranseed = int(fline)
        # np.random.seed(ranseed)

        INFECTION_PROBABILITY = dfToFloat(thresholds_df,"INFECTION_PROBABILITY")        

        for prsn in persons:

            if(prsn.quarantined_day > -1):
                prsn.quarantined_day += 1
                if(prsn.quarantined_day == quarantine_days and prsn.is_infected == False):
                    prsn.quarantined_day = -1
                    prsn.profession = prsn.initial_profession

            
            if(not prsn.is_infected):

                if(prsn.infection_level>=INFECTION_PROBABILITY):
                    prsn.is_infected = True
                    prsn.setState('Infected_notContagious')
                    #print("\n\n\nNew Guy: {} by {} - Profession: {}".format(prsn.id, prsn.infected_by, prsn.profession))

                    #if(prsn.profession=='Isolated'):
                        #print("Bad luck dude! Days: {} TaskCnt: {} QDAY: {}".format(prsn.infected_days, len(prsn.tasks), prsn.quarantined_day))
                        #print(prsn.tasks)
            else:

                prsn_state = prsn.getState()
                prsn.infected_days += 1

                if(prsn_state == 'contagious_symptomatic'):
                    prsn.hospitalize()

                prsn.die()

                if(prsn_state == 'Dead'):
                    #person dead do nothing but immunity and stuff deal later
                    dummy = 1
                else:
                    if(prsn.is_alive==False):
                        prsn.setState('Dead')
                    elif(prsn.infected_days==4):
                        prsn.setState('contagious_asymptomatic')
                    elif(prsn.infected_days==6):
                        prsn.setState('contagious_symptomatic')
                    # elif(prsn.infected_days==1):
                    #     prsn.setState('contagious_symptomatic')

                        #contact trace
                        if(prsn.is_traceable):
                            TRACING_STARTS_ON_DAY = 21
                            if(num_of_day>=TRACING_STARTS_ON_DAY):
                                trace_start = max(1,(num_of_day - trace_days + 1))
                                rangeday = num_of_day + 1
                                for numday in range(trace_start,rangeday):
                                    filename = 'group_info_day_' + str(numday) + '.p'                    
                                    groupfile = open(filename,'rb')
                                    groupdetails = pickle.load(groupfile)
                                    groupfile.close()

                                    for hourgroup in groupdetails:
                                        record_found_prob = np.random.rand()
                                        PROBABILITY_OF_RECORD_EXISTING = 0.9
                                        if(record_found_prob < PROBABILITY_OF_RECORD_EXISTING): 
                                            grparray = hourgroup[prsn.id]
                                            for contactperson_id in grparray:
                                                #contactperson.initial_profession = contactperson.profession
                                                contactperson = persons[contactperson_id]
                                                isolated_prob = np.random.rand()
                                                if(isolated_prob < 0.5):
                                                    contactperson.profession = "Isolated"
                                                else:
                                                    contactperson.profession = "Unemployed"
                                                contactperson.quarantined_day = 0
                                                #print("{} has been tracked down!".format(contactperson.id))
                    






            

            