class Task:

    def __init__(self, name, start_time, end_time):

        self.name = name
        self.start_time = start_time
        self.end_time = end_time


    def __lt__(self, other):

        
            if(self.start_time < other.start_time):
                return True
            elif(self.start_time > other.start_time):
                return False
            else:
                if(self.end_time < other.end_time):
                    return True
                elif(self.end_time > other.end_time):
                    return False
                else:
                    return False

    def __str__(self):

        return 'Task {}, starts at {} and ends at {}'.format(self.name, self.start_time, self.end_time)