from Random.normal_distribution import randn

class Person:

    def __init__(self, id, name, age, profession, family_id, profession_df, is_traceable, print_prompt=False):

        self.id = id
        self.name = name
        self.age = age
        
        self.profession = profession

        self.family_id =  family_id
        self.profession_group_id = None

        self.tasks = []
        self.actions = []

        self.current_task = None

        self.is_alive = True
        self.is_infected = False
        
        self.infection_level = 0.0
        self.infected_by = None
        self.infected_by_updt = 0
        self.infected_days = 0

        self.awareness_level = 0.0
        self.protection_level = 0.0

        self.state = 'Not_infected'
        self.initial_profession = profession
        self.quarantined_day = -1

        self.is_traceable = is_traceable

        

        if(print_prompt):
            print('A person named {}, {} years old with profession = {} has been created'.format(self.name,self.age,self.profession))


    def selectProfession(self,profession_df):

        # change this according to central percentage

        probable_profession = None
        max_prob = -1.0

        for index, row in profession_df.iterrows():
            
            prob = randn(row["min_prob"],row["max_prob"]) 

            if(prob>max_prob):
                
                max_prob = prob
                probable_profession = row["name"]

        if(max_prob<0.5):
            probable_profession = 'Unemployed'
    
        return probable_profession


    def setTasks(self, tasks):

        self.tasks = tasks

    def setActions(self, actions):

        self.actions = actions

    def getActions(self):

        return self.actions

    def updateCurrentTask(self, hour):

        for tsk in self.tasks:

            if(tsk.start_time<=hour and hour<tsk.end_time):

                self.current_task = tsk

                return


    def setProfessionGroupId(self, profession_group_id):

        self.profession_group_id = profession_group_id

    
    def hospitalize(self):

        if(self.is_infected and self.profession!="Hospitalized"):
            tmp = randn(0,1)
            #print("WOWOWOWOWOWOOWOWO   when hosp : " + str(tmp))
            if(tmp>0.75):
                
                self.profession = "Hospitalized"

                print('Person {} has been hospitalized'.format(self.id))

    def die(self):

        if(self.infected_days>15):

            if(randn(0,1)>0.5):

                self.is_alive = False

                print('Person {} has died'.format(self.id))

    def raiseAwareness(self):

        if(randn(0,1)>0.5):

            self.awareness_level = min(self.awareness_level + randn(0,1), 1.0)

    
    def becomeProtected(self):

        randnum = randn(0,1)
        extra_protection = 0.00
        if(self.profession=='Hospitalized' or self.profession=='Doctor'):
            
            if(randnum>0.7):
                self.protection_level = 0.5 + extra_protection
            elif(randnum>0.3):
                self.protection_level = 0.25 + extra_protection
            else:
                self.protection_level = 0.1 + extra_protection
        else:
            if(randnum>0.7):
                self.protection_level = min(randn(0, self.awareness_level),0.25 + extra_protection)

    def setState(self,infected_state):
        self.state = infected_state

    def getState(self):
        return self.state


