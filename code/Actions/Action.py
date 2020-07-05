class Action:

    def __init__(self, person_id, name, timestamp, min_prob_affect, max_prob_affect, min_effect_others, max_effect_others, min_effect_self, max_effect_self):
        
        self.person_id = person_id
        self.name = name
        self.timestamp = timestamp
        self.min_prob_affect = min_prob_affect
        self.max_prob_affect = max_prob_affect
        self.min_effect_others =  min_effect_others
        self.max_effect_others =  max_effect_others
        self.min_effect_self =  min_effect_self
        self.max_effect_self =  max_effect_self

    def __lt__(self, other):

        return self.timestamp < other.timestamp

    def __str__(self):

        return 'Action : {} by Person {}\nTime Stamp : {}\nPrbability Affect : {}~{}\nEfect Others : {}~{}\nEffect Self : {}~{}\n'.format(self.name, self.person_id,
                   self.timestamp,
                   self.min_prob_affect,self.max_prob_affect,
                   self.min_effect_others,self.max_effect_others,
                   self.min_effect_self,self.max_effect_self)
        