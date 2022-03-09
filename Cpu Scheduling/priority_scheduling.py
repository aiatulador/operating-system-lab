num_process = int(input("Enter the number of Processes: "))

burst_time = []
priority = []

process = 1

for i in range(num_process):
  print("For Process Number P",process,": ")
  burst_time.append(int(input("Burst Time: ")))
  priority.append(int(input("Priority: ")))
  process += 1

x = zip(priority,burst_time)
sorted_x = sorted(x)
y_sorted =[element for _,element in sorted_x]

wait_time= []
average_wait = 0

wait_time.insert(0,0)

for i in range(1,len(y_sorted)):
  wait_time.insert(i,(wait_time[i-1]+ y_sorted[i-1]))
  average_wait += wait_time[i]

average_wait = float(average_wait / num_process)

print("\n\nAverage Waiting Time: ",average_wait,"\n\n")

print("Grant Chart: ")
for j in range(0, num_process):
  print(wait_time[j],"ms  " "p", priority[j], end="|")



