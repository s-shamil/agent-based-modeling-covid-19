from Groups.Group import Group
from DatabaseAdaptor.utils import dfToInt
import numpy as np
import random

class GroupManager :

    def __init__(self):

        pass


    @staticmethod
    def assignGroups(persons, preferences_df, tracing_percentage, num_of_day):

        person_group = {}
        # fline = open("seed.txt").readline().rstrip()
        # ranseed = int(fline)
        # np.random.seed(ranseed)
        # random.seed(ranseed)
        groupDict = {}

        transport_free_seats = []

        n_transport = dfToInt(preferences_df, "n_transport")
        transport_seat_limit = dfToInt(preferences_df, "transport_seat_limit")
        n_events = dfToInt(preferences_df, "n_events")
        quarantine_start = dfToInt(preferences_df, "quarantine_start")

        for i in range(n_transport):            

            transport_free_seats.extend([i]*transport_seat_limit)


        for prsn in persons:

            if not prsn.is_alive:

                continue


            if(prsn.current_task.name=="Stay Home"):

                group_id = "F-{}".format(prsn.family_id)


            elif(prsn.current_task.name=="Go to Work" or prsn.current_task.name=="Returns Home"):

                selected_transport = random.choice(transport_free_seats)
                transport_free_seats.remove(selected_transport)

                group_id = "T-{}".format(selected_transport)
                

            elif(prsn.current_task.name=="Work"):

                group_id = "W-{}".format(prsn.profession_group_id)                
            

            elif(prsn.current_task.name=="Attend Event"):
                group_id = "E-{}".format(np.random.randint(0,n_events))
                '''
                effort = 0
                while True:
                    group_id = "E-{}".format(np.random.randint(0,n_events))
                    if(num_of_day >= quarantine_start):
                        if(group_id in groupDict):
                            if(len(groupDict[group_id].persons)<15):
                                break
                        else:
                            break
                    else:
                        break

                    effort +=1
                    if(effort==3):
                        break
                '''
                


            elif(prsn.current_task.name=="Stay Hospital"):
                group_id = "H"
            elif(prsn.current_task.name=="Treat Patients"):
                group_id = "H"


            if(group_id not in groupDict):

                groupDict[group_id] = Group(group_id)

            groupDict[group_id].addPerson(prsn)


        for grpid in groupDict:
            grouparr = groupDict[grpid]
            personarr = grouparr.persons
            
            personid_arr = []
            for pers in personarr:
                decision_var = np.random.rand()
                if(decision_var<tracing_percentage and pers.is_traceable):
                    personid_arr.append(pers.id)

            for prsn in personarr:
                #print(prsn.id)
                #person_group[prsn.id] = personarr
                person_group[prsn.id] = personid_arr
        #print(person_group)

        groups = []

        for grp_id in groupDict:

            groups.append(groupDict[grp_id])

        groupDict = {}


        for grp in groups:

            grp.updatePersonMapper()

            grp.updateProximity()



        return groups,person_group


    @staticmethod
    def updateActions(grp):

        print('in')
        grp.updateActions()
        print('in',grp.persons[0])