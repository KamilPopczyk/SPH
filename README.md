# Task1

Solution of Task1 - Sprint Planning Helper

## Getting Started

These instructions will get you how to run.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6
```

### Run

In commandline:

```
sprint-planning-helper.py [file_with_tasks] KSP
```

## Tests

Tests were done with various amount of data.

### Generete test data

Simple script to generete dataL

```python
import random

def make_csv_file(how_many):
    with open("csv_with_task.csv", "w") as file:
        file.write("task_id,story_points,KSP \n")

        for x in range(how_many):
            file.write(str(x) + ",")
            file.write(str(random.randint(1, 30)) + ",")
            file.write(str(random.randint(1, 30)) + "\n")

        file.close()
    return True

def main():
    if make_csv_file(2500):
        print("Success.")
    else:
        print("Something went wrong.")


if __name__ == '__main__':
    main()
```

### Results
Results is given in set: data_size time( in ms )
* 10	0,124013424
* 100	0,454795361
* 500	2,259378433
* 1000	3,990688324
* 2500	10,28289795
* 5000	20,54651022
* 10000	40,02947807

Computational complexity is nlog(n)

## Algorithm

Problem with compering given task was solved with counting value. Value shows how many KSP is worth in each tasks. 
