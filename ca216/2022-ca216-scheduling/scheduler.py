# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.


def main_scheduler(tasks):
    """Schedules tasks in a given queue for every algorithm except round robin."""
    timer = 0
    avgTurnAround = 0               # store the turn around times to calculate avg
    waitingTime = 0                 # store the waiting times to calculate avg
    length = tasks.qsize()          # get the length of the queue

    # loop through the queue using the built-in queue method empty()
    while tasks.empty() is not True:
        curTask = tasks.get()           # get the current task and store it in curTask
        # print the current task's name, time waited to execute, run time and turn around time.
        print(f"Process {curTask['name']} waited for {timer} MS to run and ran for {curTask['burst']} MS. "
              f"It had a turn-around time of {curTask['burst'] + timer} MS.")

        waitingTime += timer
        avgTurnAround += curTask['burst'] + timer
        timer += curTask['burst']

    end_print(avgTurnAround, waitingTime, length)


def scheduler_round_robin(tasks, timeQuantum):
    """Schedules tasks in a given queue for round robin only."""
    timer = 0
    avgTurnAround = 0  # store the turn around times to calculate avg
    waitingTime = 0  # store the waiting times to calculate avg
    length = tasks.qsize()  # get the length of the queue

    # create a copy of the burst times to print the correct burst time at the end
    burstTimes = []
    for i in tasks.queue:
        burstTimes.append([i['name'], i['burst']])

    # loop through the queue using the built-in queue method empty()
    while tasks.empty() is not True:
        curTask = tasks.get()
        # if task burst is greater than time quantum, remove time quantum from burst
        # and add the task to the end of the queue
        if curTask['burst'] > timeQuantum:
            curTask['burst'] -= timeQuantum
            timer += timeQuantum
            tasks.put(curTask)
        else:
            # find the full burst time of the task before it was scheduled
            taskName = curTask['name']
            fullBurst = 0
            for i in range(length):
                if burstTimes[i][0] == taskName:
                    fullBurst = burstTimes[i][1]
                    break

            # print the current task's name, original burst time, time waited to execute, run time and turn around time.
            print(f"Process {curTask['name']} ran for {fullBurst} MS. "
                  f"It had a waiting time of {timer - fullBurst + curTask['burst']} MS. "
                  f"It had a turn-around time of {curTask['burst'] + timer}.")

            waitingTime += timer - fullBurst + curTask['burst']
            avgTurnAround += curTask['burst'] + timer
            timer += curTask['burst']

    end_print(avgTurnAround, waitingTime, length)


def scheduler(schType, tasks, timeQuantum=10):
    """Schedules tasks in a given queue for either round robin or non-round robin."""
    if schType == "rr":
        scheduler_round_robin(tasks, timeQuantum)
    else:
        main_scheduler(tasks)


def end_print(avgTurnAround, waitingTime, length):
    """Prints the average turn around time and average waiting time."""
    print(f"\nAverage Turn Around time is: {avgTurnAround / length} milliseconds."
          f"\nAverage Waiting time is: {waitingTime / length} milliseconds.")
