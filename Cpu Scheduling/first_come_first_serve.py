num_process = int(input("Enter the number of Processes: "))

burst_time = []
sequence = 1

for i in range(num_process):
  print("For process No ", sequence)
  burst_time.append(int(input("Burst Time: ")))
  sequence += 1
print("\n")

wait_time = []
avg_wait_time = 0
wait_time.insert(0,0) #insert value 0 in 0 index

for j in range(1, len(burst_time)):
  wait_time.insert(j,(wait_time[j-1])+ burst_time [j-1]) 
  avg_wait_time += wait_time[j]


avg_wait_time = float(avg_wait_time/num_process)

process = 1

print("Grand Chart:")
for k in range(0, num_process):
    print(wait_time[k],"ms", "P",process,burst_time[k]+wait_time[k],"ms",end = "  |  ")
    process += 1

print("\n\nAverage Waiting Time = ", avg_wait_time, "ms")