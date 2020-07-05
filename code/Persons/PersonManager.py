from Random.string_generator import rands
from Random.normal_distribution import randni
from Persons.Person import Person
from DatabaseAdaptor.utils import dfToInt
import numpy as np
import random
from tqdm import tqdm

class PersonManager:

    def __init__(self):

        pass

    @staticmethod
    def generatePersons(n_persons, profession_df, preferences_df, smartphone_owner_percentage):

        # fline = open("seed.txt").readline().rstrip()
        # ranseed = int(fline)
        # random.seed(ranseed)
        min_age = dfToInt(preferences_df,"min_age")
        max_age = dfToInt(preferences_df,"max_age")
        min_family_size = dfToInt(preferences_df,"min_family_size")
        max_family_size = dfToInt(preferences_df,"max_family_size")
        min_name_length = dfToInt(preferences_df,"min_name_length")
        max_name_length = dfToInt(preferences_df,"max_name_length")

        persons = []

        profession_age_mapping = {}
        profession_options = []

        for ind, row in profession_df.iterrows():

            profession_age_mapping[row["name"]] = {'min_age':row["min_age"], 'max_age':row["max_age"]}
            profession_options.extend([row["name"]]*(int(float(row["percentage"])*n_persons)))


        family_id = 0
        family_size = 0
        while(family_size<=0):
            family_size = randni(min_family_size, max_family_size)

        smartphone_owner_cnt = 0
        for i in tqdm(range(0,n_persons), desc='#Persons'):


            if(family_size>0):
                
                try:
                    profession_selected = random.choice(profession_options)
                    profession_options.remove(profession_selected)
                except:
                    print(i)
                    profession_selected = 'Unemployed'
                
                is_traceable = False 
                # randomx = np.random.rand()
                # if(randomx < smartphone_owner_percentage):
                #     is_traceable = True
                #     smartphone_owner_cnt += 1
                # else:
                #     is_traceable = False


                persons.append(Person(i, rands(randni(min_name_length, max_name_length)), randni(profession_age_mapping[profession_selected]['min_age'], profession_age_mapping[profession_selected]['max_age']), profession_selected ,family_id,profession_df, is_traceable))

                family_size -= 1

            if(family_size==0):

                family_id += 1
                while(family_size<=0):
                    family_size = randni(min_family_size, max_family_size)

        print("smartphone owner: " + str(smartphone_owner_cnt))
        PersonManager.assignProfessionGroup(persons, preferences_df)

        return persons


    @staticmethod
    def assignProfessionGroup(persons, preferences_df):

        # fline = open("seed.txt").readline().rstrip()
        # ranseed = int(fline)
        # np.random.seed(ranseed)
        worker_ids = []

        for prsn in persons:

            if(prsn.profession=='Service'):

                worker_ids.append(prsn.id)

        
        np.random.shuffle(worker_ids)
        n_workgroup = dfToInt(preferences_df,"n_workgroup")
        worker_per_workgroup = len(worker_ids)//n_workgroup

        for i in range(len(worker_ids)):

            persons[worker_ids[i]].setProfessionGroupId(min(i//worker_per_workgroup,n_workgroup))


    @staticmethod
    def initialInfection(persons, n_infected_init):

        # fline = open("seed.txt").readline().rstrip()
        # ranseed = int(fline)
        # np.random.seed(ranseed)

        while(n_infected_init > 0):

            person_id = np.random.randint(0,len(persons))

            while persons[person_id].is_infected == True:

                person_id = np.random.randint(0,len(persons))

            persons[person_id].is_infected = True
            persons[person_id].setState('Infected_notContagious')
            print('Person {} is initially infected'.format(person_id))
            n_infected_init -= 1

