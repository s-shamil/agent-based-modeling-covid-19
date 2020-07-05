from Random.normal_distribution import randn
from DatabaseAdaptor.utils import dfToFloat

class GroupSimulator:

    def __init__(self):
        pass 

    @staticmethod

    def groupInteraction(grp, thresholds_df):


        ACTION_AFFECTING_PROBABILITY = dfToFloat(thresholds_df,"ACTION_AFFECTING_PROBABILITY")
        ACTION_INFECT_THRESHOLD = dfToFloat(thresholds_df,"ACTION_INFECT_THRESHOLD")

        next_timestamp = 10


        for actn in grp.actions:

            if(actn.timestamp>=next_timestamp):
                
                grp.updateProximity()

                next_timestamp += 10

            acting_person_id = actn.person_id
            acting_person = grp.persons[grp.person_mapper[acting_person_id]]
            

            for prsn in grp.persons:

                if(randn(actn.min_prob_affect,actn.max_prob_affect)>ACTION_AFFECTING_PROBABILITY):
                    if(prsn.id==acting_person_id):
                        if(actn.min_effect_self >= 0):
                        
                            infection = (1-prsn.protection_level) * randn(actn.min_effect_self,actn.max_effect_self)

                            #print(infection)
                            if(infection>ACTION_INFECT_THRESHOLD):

                                prsn.infection_level = max(min(prsn.infection_level+infection, 1),0)
                                #print("\n" + str(actn.name) + " the infection case for self infection is - " + str(prsn.infection_level))
                        else:

                            infection = (1-prsn.protection_level) * randn(actn.min_effect_self,actn.max_effect_self)
                            #print("the infection case is - " + str(infection))
                            infection_pos = (-1)*infection

                            if(infection_pos>ACTION_INFECT_THRESHOLD):
                             
                                prsn.infection_level = max(min(prsn.infection_level+infection, 1),0)

                    else:
                        if(acting_person.state == 'contagious_asymptomatic' or acting_person.state == 'contagious_symptomatic'):

                            if(not prsn.is_infected):

                                #print("the people - " + str(acting_person_id) + " " +str(actn.person_id) + " " + str(prsn.id))
                                proximit = grp.getProximity(acting_person_id,prsn.id)
                                #proximit = 1

                                infection = (1-prsn.protection_level) * randn(actn.min_effect_others,actn.max_effect_others) 
                                #print("infection before = " + str(infection) + " proximity - " + str(proximit))

                                infection = infection * proximit


                                if(infection>ACTION_INFECT_THRESHOLD):

                                    prsn.infection_level = max(min(prsn.infection_level+infection, 1),0)

                                    prsn.infected_by = acting_person_id

                                    prsn.infected_by_updt += 1

        return grp


