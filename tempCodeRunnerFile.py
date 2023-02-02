# Round robin

class RR:
    def __init__(self,processes):
        self.processes = processes
        self.av_turn_around_time = 0
        self.av_waiting_time = 0

    def completion_time(self):
        completion_times = []
        current_time = 0        
        processes = []
        quantum = 2
        for i,p in enumerate(self.processes):
            a = self.processes[i][1]
            b = self.processes[i][2]
            c = self.processes[i][0]
            d = [a,b,c]
            processes.append(d)
        remaining_processes = processes
        print(remaining_processes)

        while remaining_processes:
            ready_processes = []
            for p in remaining_processes:
                if p[0] <= current_time:
                    ready_processes.append(p)
            print(ready_processes)
            if not ready_processes:
                next_arrival_time = min(p[0] for p in remaining_processes)
                current_time = next_arrival_time
                continue
            process = ready_processes[0]
            processs_time_left = (process[1] - quantum)
            if processs_time_left <0:
                running_time = current_time + process[1]
                process[1] = 0
                remaining_processes.remove(process)
                for p in remaining_processes:
                    if p[0] <= current_time:
                        ready_processes.append(p)

            elif processs_time_left == 0:
                running_time = current_time + quantum
                process[1] = 0
                remaining_processes.remove(process)
                for p in remaining_processes:
                    if p[0] <= current_time:
                        ready_processes.append(p)

            elif processs_time_left >= 0:
                remaining_processes.remove(process)
                remaining_processes.append(process)
                running_time = current_time + quantum
                process[1] = processs_time_left
                for p in remaining_processes:
                    if p[0] <= current_time:
                        ready_processes.append(p)
            
            # completion_times.append([process[2],process[0],process[1],completion_time])
            current_time = running_time
            print(current_time)
        # self.processes = completion_times

    # def turn_around_time(self):
    #     for i,p in enumerate(self.processes):
    #         self.processes[i].append(self.processes[i][3] - self.processes[i][1])
    
    # def waiting_time(self):
    #     for i,p in enumerate(self.processes):
    #         self.processes[i].append(self.processes[i][4] - self.processes[i][2])

    # def average_turn_around_time(self):
    #     a = 0
    #     for i,p in enumerate(self.processes):
    #         a += self.processes[i][4]
    #     self.av_turn_around_time = a/len(self.processes)

    # def average_waiting_time(self):
    #     a = 0
    #     for i,p in enumerate(self.processes):
    #         a += self.processes[i][5]
    #     self.av_waiting_time = a/len(self.processes)

    # def printing(self):
    #     print("\n-------------------SJF-------------------")
    #     print("PID\t"+"AT\t" + "BT\t" + "CT\t" + "TAT\t"+ "WT\t")
    #     for p in self.processes:
    #         print(str(p[0]) + "\t" + str(p[1]) + "\t" + str(p[2]) + "\t" + str(p[3])+ "\t" + str(p[4])+ "\t" + str(p[5]))

    #     print("\nAverage Waiting Time is : " + str(self.av_waiting_time))
    #     print("Average Turn Around Time is : " + str(self.av_turn_around_time)+"\n")


if __name__ == "__main__":

    processes = [['p1',0,5],['p2',1,4],['p3',2,2],['p4',4,1]]
    # to take input from user, comment above array and uncomment below commented code 
    # processes = []
    # n = int(input("Enter number of processes : "))
    # for i in range(n):
    #     a = input("Enter " + str(i) + " process id : ")
    #     b = int(input("Enter " + str(i) + " process arrival time : "))
    #     c = int(input("Enter " + str(i) + " process burst time : "))
    #     d = [a,b,c]
    #     processes.append(d)

    s = RR(processes)
    s.completion_time()
    # s.turn_around_time()
    # s.waiting_time()
    # s.average_turn_around_time()
    # s.average_waiting_time()
    # s.printing()