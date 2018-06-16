import sys
import os


class Task:  # define task with parameters
    def __init__(self, task_id, story_points, KSP):
        self.task_id = task_id
        self.story_points = story_points
        self.KSP = KSP
        self.value = 0


class SprintPlanningHelper:
    def __init__(self):
        self.TaskList = []

    def load_csv_file(self, filename):
        if os.path.isfile(filename):  # exist ?
            with open(filename, "r") as fileData:
                fileData.__next__()  # skip header
                for dataLine in fileData:
                    dataLine = dataLine.replace("\n", "")  # new line?  I don't need that
                    currentline = dataLine.split(",")
                    if (len(currentline) == 3):  # correct data
                        task = Task(int(currentline[0]), int(currentline[1]), int(currentline[2]))
                        self.TaskList.append(task)
                    else:
                        print("Too few data in file.")
                        return False
        else:
            print("File don't exist.")
            return False

        return self.TaskList

    def find_tasks_aproximation(self, velocity):  #  velocity >= the sum of story points
        found_tasks = []
        actual_sum_of_story_points = 0
        # count value , value = KSP / story_points
        for task in self.TaskList:
            task.value = task.KSP / task.story_points
        # sort them
        task_list_copy = self.TaskList
        task_list_copy.sort(key=lambda Task: Task.value, reverse=True)
        # let's find tasks
        for task in task_list_copy:
            if task.story_points + actual_sum_of_story_points <= velocity:
                found_tasks.append(task)
                actual_sum_of_story_points += task.story_points
            else:
                break

        return found_tasks





def main():
    arguments = sys.argv

    # tasklist = loadCSVFile("csv_with_task.csv")
    helper = SprintPlanningHelper()
    helper.load_csv_file("csv_with_task.csv")
    tasklist = helper.find_tasks_aproximation(13)

    for t in tasklist:
        print(t.task_id)

    if len(arguments) == 0:
        print("No arguments ! ")

    else:
        print("Arguments ok")

if __name__ == '__main__':
    main()
