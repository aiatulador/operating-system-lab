num_process = int(input("Enter the number of Processes: "))


x = num_process


burst_time_for_pro = []
for i in range(0, x):
    print("For process no P" + str(i + 1) + " :")
    bt = int(input("Burst Time: "))
    burst_time_for_pro.append(bt)

sum = 0
tmps = []
indexes = []

burst_time_for_process = []

for bt in burst_time_for_pro:
    burst_time_for_process.append(bt)

burst_time_for_process.sort()

for i in range(0, x - 1):
    min = burst_time_for_process[i]  # [2, 3, 6, 21]
    ind = burst_time_for_pro.index(min)  # [21, 3, 6, 2]
    tm = 0
    for j in range(0, i):
        tm = tm + burst_time_for_process[j]
    sum = sum + min + tm
    tmps.append(min + tm)
    indexes.append(ind)

print("\n\nThe Average Waiting time: (0+", sep='', end='', flush=True)
for i in range(0, len(tmps)):
    print(str(tmps[i]) + "", sep='', end='', flush=True)
    if i != x - 2:
        print("+", sep='', end='', flush=True)

print("/" + str(x) + ")", "= " + "{:.2f}".format(sum / x),"ms","\n\n")
#print("\t\t\t\t =" + "{:.2f}".format(sum / x),"ms")

print("Grant Chart: ", sep=' ', end='', flush=True)
for i in range(0, x):
    if i != x - 1:
        print(" P" + str(indexes[i] + 1) + " | " + str(tmps[i]) ,"ms"+ " ", sep=' ', end=':', flush=True)
    if i == x - 1:
        ind = burst_time_for_pro.index(burst_time_for_process[i])
        print(" P" + str(ind + 1) + " | " + str(tmps[i - 1]+ burst_time_for_process[i]),"ms" + " ", sep=' ', end=':', flush=True)