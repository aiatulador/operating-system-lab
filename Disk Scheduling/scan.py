queue = list(map(int, input('Enter Queue : ').split(',')))
header = int(input('Head Starts : '))

def main_process(length_of_queue, head_start, array):
    second_value = head_start
    Total_distance = 0
    path = str(head_start)
    head_to_lower_bound = []
    head_to_upper_bound = []
    a = int(input('Upper Bound : '))
    b = int(input('Lower Bound : '))
    X_path = ''

    for i in range(0, length_of_queue):
        if int(array[i]) < head_start:
            head_to_lower_bound.append(int(array[i]))
        else:
            head_to_upper_bound.append(int(array[i]))
    empty = []
    for s in range(0, len(head_to_upper_bound) - 1):
        for y in range(0, len(head_to_upper_bound) - 1):
            if head_to_upper_bound[y] > head_to_upper_bound[y + 1]:
                empty = head_to_upper_bound[y]
                head_to_upper_bound[y] = head_to_upper_bound[y + 1]
                head_to_upper_bound[y + 1] = empty
    empty = []
    for s in range(0, len(head_to_lower_bound) - 1):
        for y in range(0, len(head_to_lower_bound) - 1):
            if head_to_lower_bound[y] < head_to_lower_bound[y + 1]:
                empty = head_to_lower_bound[y]
                head_to_lower_bound[y] = head_to_lower_bound[y + 1]
                head_to_lower_bound[y + 1] = empty

    for z in range(0, len(head_to_lower_bound)):
        if int(head_to_lower_bound[z]) > second_value:
            path = path + ' ' + str(head_to_lower_bound[z])

            Total_distance = Total_distance + (int(head_to_lower_bound[z]) - second_value)
            X_path = X_path + '(' + str(head_to_lower_bound[z]) + '-' + str(second_value) + ')'
            second_value = int(head_to_lower_bound[z])
        else:
            path = path + ' ' + str(head_to_lower_bound[z])

            Total_distance = Total_distance + (second_value - int(head_to_lower_bound[z]))
            X_path = X_path + '(' + str(second_value) + '-' + str(head_to_lower_bound[z]) + ')'
            second_value = int(head_to_lower_bound[z])

        X_path = X_path + '+'

    Total_distance = Total_distance + (second_value - b)
    X_path = X_path + '(' + str(second_value) + '-' + str(b) + ')'
    X_path = X_path + '+'
    second_value = b
    path = path + ' ' + str(b)
    for x in range(0, len(head_to_upper_bound)):
        if int(head_to_upper_bound[x]) > second_value:
            path = path + ' ' + str(head_to_upper_bound[x])
            Total_distance = Total_distance + (int(head_to_upper_bound[x]) - second_value)
            X_path = X_path + '(' + str(head_to_upper_bound[x]) + '-' + str(second_value) + ')'
            second_value = int(head_to_upper_bound[x])
        else:
            path = path + ' ' + str(head_to_upper_bound[x])
            Total_distance = Total_distance + (second_value - int(head_to_upper_bound[x]))
            X_path = X_path + '(' + str(second_value) + '-' + str(head_to_upper_bound[x]) + ')'
            second_value = int(head_to_upper_bound[x])
        if x == len(head_to_upper_bound) - 1:
            break
        else:
            X_path = X_path + '+'

    print('\nCalculation Path : ' + X_path)
    print('\nTotal Distance : ' + str(Total_distance),"cylinders")
    print('\nPath : ' + path)


queue_for_scan = queue
length_queue_for_scan = len(queue_for_scan)

main_process(length_queue_for_scan, header, queue_for_scan)