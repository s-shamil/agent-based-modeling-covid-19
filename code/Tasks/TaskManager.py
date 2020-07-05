from Random.normal_distribution import randn
from Tasks.Task import Task

class TaskManager:

    def __init__(self):

        pass


    @staticmethod
    def generateTasks(task_df):

        taskList = []
        

        for index, row in task_df.iterrows():

            prob = randn(row["min_prob"],row["max_prob"]) 

            if(prob<0.5):

                continue

            start_time = round(randn(row["min_start_time"],row["max_start_time"]))
            duration = round(randn(row["min_duration"],row["max_duration"]))
            
            taskList.append(Task(row["task"], start_time, start_time+duration))

        taskList = TaskManager.refineTaskDuration(taskList)

        return taskList


    @staticmethod
    def printTasks(tasks):

        print('------------------')

        for tsk in tasks:

            print(tsk.name,tsk.start_time,tsk.end_time)

        print('------------------')


    @staticmethod
    def refineTaskDuration(tasks):            # for now a simplified, very rudimentary interval covering has been done

        # fixing same start time

        tasks.sort()

        last_start_time = -1

        for i in range(len(tasks)):

            if(last_start_time == tasks[i].start_time):

                tasks[i].start_time += 1
                tasks[i].end_time = min(tasks[i].end_time + 1, 23)

            last_start_time = tasks[i].start_time

        
        # solving overlaps

        newTasks = []

        i = 0

        while i<len(tasks):

            if(tasks[i].start_time>=tasks[i].end_time):

                i += 1
                continue

            elif((i<(len(tasks)-1)) and (tasks[i].end_time>tasks[i+1].start_time)):

                newTasks.append(Task(tasks[i].name,tasks[i].start_time,tasks[i+1].start_time))

                tasks[i] = Task(tasks[i].name,tasks[i+1].end_time,tasks[i].end_time)

                
                (tasks[i],tasks[i+1]) = (tasks[i+1],tasks[i])
                                
                continue

            else:

                newTasks.append(Task(tasks[i].name,tasks[i].start_time,tasks[i].end_time))
                i += 1
                continue


        # filling up gaps

        for i in range(1,len(tasks)):

            tasks[i-1].end_time = tasks[i].start_time


        return newTasks

