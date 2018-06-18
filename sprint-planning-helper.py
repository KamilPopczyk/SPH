import sys
import os
import time


class Task:
    """Class Task store info about task"""
    def __init__(self, task_id, story_points, KSP):
        self.task_id = task_id
        self.story_points = story_points
        self.KSP = KSP
        self.value = 0


class SprintPlanningHelper:
    """SprintPlanningHelper class"""
    def __init__(self):
        self.task_list = []

    def load_csv_file(self, file_name):
        """Load csv file"""
        if os.path.isfile(file_name):  # exist ?
            with open(file_name, "r") as fileData:
                fileData.__next__()  # skip header
                for data_line in fileData:
                    data_line = data_line.replace("\n", "")  # new line?  I don't need that
                    current_line = data_line.split(",")
                    if (len(current_line) == 3):  # correct data
                        task = Task(int(current_line[0]), int(current_line[1]), int(current_line[2]))
                        self.task_list.append(task)
                    else:
                        print("Too few data in file.")
                        return False
        else:
            print("File don't exist.")
            return False

        return self.task_list

    def find_tasks_aproximation(self, velocity):  #  velocity >= the sum of story points
        """Aproximation algorithm"""
        found_tasks = []
        actual_sum_of_story_points = 0
        # count value , value = KSP / story_points
        # value represents how many KSP per one story point
        for task in self.task_list:
            task.value = task.KSP / task.story_points
        # sort them
        task_list_copy = self.task_list
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

    if len(arguments) < 3:
        print("Not enough arguments ! ")

    else:
        helper = SprintPlanningHelper()
        if helper.load_csv_file(arguments[1]) is False:
            print("Error")
        else:
            task_list = helper.find_tasks_aproximation(int(arguments[2]))
            task_list.sort(key=lambda Task: Task.task_id, reverse=False)
            i = 0
            for task in task_list:
                sys.stdout.write(str(task.task_id))
                if i < len(task_list) - 1:
                    sys.stdout.write(", ")
                i += 1

            sys.stdout.write("\n")

if __name__ == '__main__':
    main()
