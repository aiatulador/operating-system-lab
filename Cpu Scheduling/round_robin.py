def round_robin(y):
    #total_process = int(input('Enter the Number of Processes: '))
    total_process = y
    array = []
    sum_of_burst_time = 0
    index = []
    sum_arrayOf_single_process_wating_time = []
    wating_time_array = []
    for x in range(0, total_process):
        index.append(0)
        process_no = 'P' + str(x + 1)
        #burst_time = int(input('Process ' + process_no + ': ')) 
        #Process Number P",process,
        burst_time = int(input('For Process Number ' + process_no + ': ')) 
        sum_of_burst_time = sum_of_burst_time + burst_time
        single_process_array = [process_no, burst_time]
        processNo_starting_ending_wating = [process_no, 0, 0, 0]
        processNo_andItstotal_wating_time = [process_no, 0]
        array.append(single_process_array)
        wating_time_array.append(processNo_starting_ending_wating)
        sum_arrayOf_single_process_wating_time.append(processNo_andItstotal_wating_time)
    Quantam = int(input('\nQuantam number : '))

    y = 0
    wating_time = 0
    grant = '0'

    while sum_of_burst_time > y:
        for a in range(0, total_process):
            starting_time = y

            for z in range(1, Quantam + 1):
                if array[a][1] > 0:
                    y = y + 1
                    array[a][1] = array[a][1] - 1
                else:
                    index[a] = index[a] + 1

            ending_time = y
            if starting_time != ending_time:
                wating_time = starting_time - wating_time_array[a][2]
                sum_arrayOf_single_process_wating_time[a][1] = int(sum_arrayOf_single_process_wating_time[a][1]) + int(
                    wating_time)

            wating_time_array[a][1] = starting_time
            wating_time_array[a][2] = ending_time
            wating_time_array[a][3] = wating_time

            if index[a] < Quantam + 1:
                grant = grant + ' = ' + array[a][0]
                grant = grant + ' > ' + str(y)
    sum = 0
    for m in range(0, total_process):
        sum = sum + sum_arrayOf_single_process_wating_time[m][1]
    sum = sum / total_process

    print('\n\nAverage Waiting Time : ' + str(sum),"ms")
    print('\n\nGrant Chart : ' + grant, "ms")




num_process = int(input("Enter the number of Processes: "))

y= num_process

round_robin(y)