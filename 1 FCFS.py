# first come first serve

class FCFS:
    def __init__(self,processes):
        self.processes = processes
        self.av_turn_around_time = 0
        self.av_waiting_time = 0

    def sort(self):
        sorted_processes = []
        max_arrival_time = 0
        # find the max arrival time
        for i,p in enumerate(self.processes):
            if self.processes[i][1] > max_arrival_time:
                max_arrival_time = self.processes[i][1]

        # sorting job according to arrival time  
        for b in range(0,max_arrival_time+1):
            for i,p in enumerate(self.processes):
                if self.processes[i][1] == b:
                    sorted_processes.append(self.processes[i])
                else:
                    pass
        self.processes =  sorted_processes

    def completion_time(self):
        current_time = self.processes[0][1]
        for i,p in enumerate(self.processes):
            if self.processes[i][1]>current_time:
                current_time = self.processes[i][1]
            self.processes[i].append(current_time + self.processes[i][2])
            current_time = self.processes[i][3]
    
    def turn_around_time(self):
        for i,p in enumerate(self.processes):
            self.processes[i].append(self.processes[i][3] - self.processes[i][1])
    
    def waiting_time(self):
        for i,p in enumerate(self.processes):
            self.processes[i].append(self.processes[i][4] - self.processes[i][2])

    def average_turn_around_time(self):
        a = 0
        for i,p in enumerate(self.processes):
            a += self.processes[i][4]
        self.av_turn_around_time = a/len(self.processes)

    def average_waiting_time(self):
        a = 0
        for i,p in enumerate(self.processes):
            a += self.processes[i][5]
        self.av_waiting_time = a/len(self.processes)

    def printing(self):
        print("\n-------------------FCFS-------------------")
        print("PID\t"+"AT\t" + "BT\t" + "CT\t" + "TAT\t"+ "WT\t")
        for p in self.processes:
            print(str(p[0]) + "\t" + str(p[1]) + "\t" + str(p[2]) + "\t" + str(p[3])+ "\t" + str(p[4])+ "\t" + str(p[5]))

        print("\nAverage Waiting Time is : " + str(self.av_waiting_time))
        print("Average Turn Around Time is : " + str(self.av_turn_around_time)+"\n")


if __name__ == "__main__":

    processes = [['p1',5,2],['p2',2,4],['p3',3,9],['p4',4,2]]
    # to take input from user, comment above array and uncomment below commented code 
    # processes = []
    # n = int(input("Enter number of processes : "))
    # for i in range(n):
    #     a = input("Enter " + str(i) + " process id : ")
    #     b = int(input("Enter " + str(i) + " process arrival time : "))
    #     c = int(input("Enter " + str(i) + " process burst time : "))
    #     d = [a,b,c]
    #     processes.append(d)

    s = FCFS(processes)
    s.sort()
    s.completion_time()
    s.turn_around_time()
    s.waiting_time()
    s.average_turn_around_time()
    s.average_waiting_time()
    s.printing()