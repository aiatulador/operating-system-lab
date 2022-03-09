frame = int(input('Frame size: '))
referenceSTR = list(map(int, input('Reference String: ').split(',')))

frame_list = []
page_fault = 0
for value in referenceSTR:
    if len(frame_list)<frame:
        if value in frame_list:
            print('--hit--')
        else:
            page_fault+=1
            frame_list.append(value)
            print(frame_list)
    else:
        if value in frame_list:
            print('--hit--')
        else:
            page_fault+=1
            frame_list.pop(0)
            frame_list.append(value)
            print(frame_list)

print('\nNumber of page fault: ', page_fault)