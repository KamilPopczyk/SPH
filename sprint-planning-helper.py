import sys
import os


class Task:  # define task with parameters
    def __init__(self, task_id, story_points, KSP):
        self.task_id = task_id
        self.story_points = story_points
        self.KSP = KSP
    def giveTaskId(self):
        return self.task_id

def loadCSVFile(filename):
    TaskList = []
    if os.path.isfile(filename):  # exist ?
        with open(filename, "r") as fileData:
            fileData.__next__()  # skip header
            for dataLine in fileData:
                dataLine = dataLine.replace("\n", "")  # new line?  I don't need that
                currentline = dataLine.split(",")
                if(len(currentline) == 3): # correct data
                    task = Task(currentline[0], currentline[1], currentline[2])
                    TaskList.append(task)
                else:
                    print("Too few data in file.")
                    return False

    return TaskList


def main():
    arguments = sys.argv

    tasklist = loadCSVFile("csv_with_task.csv")

    for t in tasklist:
        print(t.KSP)

    if len(arguments) == 0:
        print("No arguments ! ")
    else:
        print("Arguments ok")

if __name__ == '__main__':
    main()
