class FCFS:
    def __init__(self):
        self.processes = None
        self.average_waiting_time = 0
        self.average_turn_around_time = 0

    def completion_time(self):
        # completion time for first process will be burst time of first process
        self.processes[0].append(self.processes[0][1])
        # calculating completion time for next processes
        for i,p in enumerate(self.processes):
            if i>=1:
                # calculating wainting time of 2nd job using previous burst time and waiting time
                self.processes[i].append(self.processes[i-1][2]+self.processes[i][1])   
            else:
                pass


    def waiting_time(self):
        # bt[i] + wt[i]
        # waiting time for first process will be zero
        self.processes[0].append(0)
        # calculating waiting time for next processes
        for i,p in enumerate(self.processes):
            if i>=1:
                # calculating wainting time of 2nd job using previous burst time and waiting time
                self.processes[i].append(self.processes[i-1][1]+self.processes[i-1][3])   
            else:
                pass


    def turn_around_time(self):
        # bt[i] + wt[i]
        for i,p in enumerate(self.processes):
            self.processes[i].append(self.processes[i][1]+self.processes[i][3])


    def table(self):
        # printing table of FCFS
        print("---------  FCFS  ---------")
        print("PID\t"+"BT\t" + "CT\t" + "WT\t" + "TAT\t")
        for p in self.processes:
            print(str(p[0]) + "\t" + str(p[1]) + "\t" + str(p[2]) + "\t" + str(p[3])+ "\t" + str(p[4]))


    def average_waiting_time_find(self):
        a=0
        for i,p in enumerate(self.processes):
            a+=self.processes[i][3]
        self.average_waiting_time = a/len(self.processes)
        print("\nAverage Waiting Time is : " + str(self.average_waiting_time))


    def average_turn_around_time_find(self):
        a=0
        for i,p in enumerate(self.processes):
            a+=self.processes[i][4]
        self.average_turn_around_time = a/len(self.processes) 
        print("Average Turn Around Time is : " + str(self.average_turn_around_time)+"\n")


def run():
    s = FCFS()
    # creating processes array and storing their arrival time and burst time input
    processes = []
    n = int(input("Enter number of processes : "))
    for i in range(1,n+1):
        a = input("Enter id of process " + str(i) + "  : ")
        b = int(input("Enter burst time of process " + str(i) + "  : "))
        c = [a,b]
        processes.append(c)

    # passing array to class and performing all calculations on it 
    s.processes = processes
    s.completion_time()
    s.waiting_time()
    s.turn_around_time()
    s.table()
    s.average_waiting_time_find()
    s.average_turn_around_time_find()

if __name__ == "__main__":
    run()