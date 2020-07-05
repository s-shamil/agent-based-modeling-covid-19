from Actions.ActionManager import ActionManager
import numpy as np
from DatabaseAdaptor.utils import dfToFloat


class Group:

    def __init__(self, group_name):

        self.group_name = group_name
        self.persons = []
        self.person_mapper = {}
        self.actions = []
        self.proximity = None

    def updateActions(self):

        self.clearActions()

        for prsn in self.persons:
    
            self.addActions(prsn.getActions())

        self.refineActions()

        

    def addActions(self, actns):

        self.actions.extend(actns)

    def refineActions(self):

        self.actions = ActionManager.refineActionList(self.actions)

    def clearActions(self):

        self.actions = []

    def addPerson(self, prsn):

        self.persons.append(prsn)

    def updatePersonMapper(self):

        self.person_mapper = {}

        for i in range(len(self.persons)):

            self.person_mapper[self.persons[i].id] = i


    '''
    def updateProximity(self):

        self.proximity = np.random.randn(len(self.persons),len(self.persons))        
        self.proximity = np.clip(self.proximity, 0.0, 1.0)
        return

        self.proximity = np.zeros((len(self.persons),len(self.persons)))

        locs = []

        for i in range(len(self.persons)):

            for j in range(i+1,len(self.persons)):
                
                locs.append([i,j])

        max_proximity = 1.0

        tot_locs = len(locs)
        reduction_step = int(tot_locs*0.1)
        next_reduction = reduction_step
        
        random_locs = list(range(tot_locs))
        np.random.shuffle(random_locs)

        

        for i in range(tot_locs):

            if(i==next_reduction):

                max_proximity -= 0.1
                next_reduction += reduction_step

            rand_proximity = np.random.rand() * max_proximity

            self.proximity[locs[random_locs[i]][0]][locs[random_locs[i]][1]] = rand_proximity
            self.proximity[locs[random_locs[i]][1]][locs[random_locs[i]][0]] = rand_proximity

    '''

    def updateProximity(self):
        full_random_proximity = False
        # fline = open("seed.txt").readline().rstrip()
        # ranseed = int(fline)
        # np.random.seed(ranseed)
        #max_proximity = dfToFloat(preferences_df,"max_proximity")
        #min_proximity = dfToFloat(preferences_df,"min_proximity")

        max_proximity = 1
        min_proximity = 0.5

        if full_random_proximity:
            
            self.proximity = np.random.randn(len(self.persons),len(self.persons))        
            self.proximity = np.clip(self.proximity, min_proximity, max_proximity)
            return

        self.proximity = np.zeros((len(self.persons),len(self.persons)))

        locs = []

        for i in range(len(self.persons)):

            for j in range(i+1,len(self.persons)):
                
                locs.append([i,j])

        #max_proximity = dfToFloat(preferences_df,"max_proximity")
        #min_proximity = dfToFloat(preferences_df,"min_proximity")


        tot_locs = len(locs)
        reduction_step = int(tot_locs*0.1)
        next_reduction = reduction_step
        
        random_locs = list(range(tot_locs))
        np.random.shuffle(random_locs)

        proximity_range = (max_proximity-min_proximity)
        reduction_amount = proximity_range*0.1

        

        for i in range(tot_locs):

            if(i==next_reduction):

                #max_proximity -= 0.1
                max_proximity -= reduction_amount
                next_reduction += reduction_step

           
            rand_proximity = np.random.rand() * reduction_amount

            var1 = max(max_proximity - rand_proximity, 0)
            var2 = max(max_proximity - rand_proximity, 0)

            #print("var1 - " + str(var1) + " var2 - " + str(var2))
            #var1 = 1
            #var2 = 1

            self.proximity[locs[random_locs[i]][0]][locs[random_locs[i]][1]] = var1
            self.proximity[locs[random_locs[i]][1]][locs[random_locs[i]][0]] = var2


    def getProximity(self,p1,p2):
        
        return self.proximity[self.person_mapper[p1]][self.person_mapper[p2]]