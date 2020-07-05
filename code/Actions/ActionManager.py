from Random.normal_distribution import randn
from Actions.Action import Action
from DatabaseAdaptor.utils import dfToFloat

class ActionManager:

    def __init__(self):

        pass


    @staticmethod
    def generateActions(prerson_id, action_df, thresholds_df):

        actionsList = []
        
        ACTION_OCCURRING_PROBABILITY = dfToFloat(thresholds_df,"ACTION_OCCURRING_PROBABILITY")

        for index, row in action_df.iterrows():

            cur_time = 0

            nxt_tme = int(randn(row["min_time_gap"],row["max_time_gap"]))

            cur_time += nxt_tme

            while(cur_time<60):

                prob = randn(row["min_prob"],row["max_prob"])

                if(prob<ACTION_OCCURRING_PROBABILITY):
                    
                    nxt_tme = int(randn(row["min_time_gap"],row["max_time_gap"]))
                    cur_time += nxt_tme

                    continue

                
                actionsList.append(Action(prerson_id, row["action"],cur_time,row["min_prob_affect"],row["max_prob_affect"],row["min_effect_others"], row["max_effect_others"], row["min_effect_self"], row["max_effect_self"]))

                nxt_tme = int(randn(row["min_time_gap"],row["max_time_gap"]))
                cur_time += nxt_tme
            
        return actionsList


    @staticmethod
    def printActions(actions):

        print('------------------')

        for actn in actions:
            
            print(actn)
            
        print('------------------')


    @staticmethod
    def refineActionList(actions):

        actions.sort()

        return actions

