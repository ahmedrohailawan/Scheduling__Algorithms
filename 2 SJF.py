# Shortest job first

class SJF:
    def __init__(self,processes):
        self.processes = processes
        self.av_turn_around_time = 0
        self.av_waiting_time = 0

    def completion_time(self):
        completion_times = []
        current_time = 0        
        processes = []
        for i,p in enumerate(self.processes):
            a = self.processes[i][1]
            b = self.processes[i][2]
            c = self.processes[i][0]
            d = (a,b,c)
            processes.append(d)
        remaining_processes = processes

        while remaining_processes:
            ready_processes = [p for p in remaining_processes if p[0] <= current_time]
            ready_processes.sort(key=lambda x: x[1])
            if not ready_processes:
                next_arrival_time = min(p[0] for p in remaining_processes)
                current_time = next_arrival_time
                continue
            process = ready_processes[0]
            completion_time = current_time + process[1]
            completion_times.append([process[2],process[0],process[1],completion_time])
            remaining_processes.remove(process)
            current_time = completion_time
        self.processes = completion_times

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
        print("\n-------------------SJF-------------------")
        print("PID\t"+"AT\t" + "BT\t" + "CT\t" + "TAT\t"+ "WT\t")
        for p in self.processes:
            print(str(p[0]) + "\t" + str(p[1]) + "\t" + str(p[2]) + "\t" + str(p[3])+ "\t" + str(p[4])+ "\t" + str(p[5]))

        print("\nAverage Waiting Time is : " + str(self.av_waiting_time))
        print("Average Turn Around Time is : " + str(self.av_turn_around_time)+"\n")


if __name__ == "__main__":

    processes = [['p1',2,4],['p2',1,2],['p3',3,3],['p4',4,5]]
    # to take input from user, comment above array and uncomment below commented code 
    # processes = []
    # n = int(input("Enter number of processes : "))
    # for i in range(n):
    #     a = input("Enter " + str(i) + " process id : ")
    #     b = int(input("Enter " + str(i) + " process arrival time : "))
    #     c = int(input("Enter " + str(i) + " process burst time : "))
    #     d = [a,b,c]
    #     processes.append(d)

    s = SJF(processes)
    s.completion_time()
    s.turn_around_time()
    s.waiting_time()
    s.average_turn_around_time()
    s.average_waiting_time()
    s.printing()