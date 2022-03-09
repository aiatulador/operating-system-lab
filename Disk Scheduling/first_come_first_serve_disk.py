queue = list(map(int, input('Enter Queue : ').split(',')))
header = int(input('Head Starts : '))

def sum_of_list(x):
  total = 0
  for val in x:
    total = total + val
  print('\nTotal Distance: ',total,' cylinders\n')

fcfs = queue
head_start = header

fcfs.insert(0, header)
print('Path: ',fcfs,'\n')

temp = [0]

for i in range(1,len(fcfs)):
    if i == len(fcfs)-1:
        print('({}-{})'.format(fcfs[i],fcfs[i-1]))
    else:
        print('({}-{})'.format(fcfs[i],fcfs[i-1]),end='+')
    temp.append(abs(fcfs[i]-fcfs[i-1]))


#print(temp)
sum_of_list(temp)