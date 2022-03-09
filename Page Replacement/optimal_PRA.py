frame = int(input('Frame size: '))
referenceSTR = list(map(int, input('Reference String: ').split(',')))


frame_list_OPA = []
page_fault_OPA = 0

for value in referenceSTR:
    idx = []
    tmp_ls = referenceSTR[referenceSTR.index(value)+1:]
    
    if len(frame_list_OPA)<frame:
        if value in frame_list_OPA:
            print('--hit--')
        else:
            page_fault_OPA+=1
            frame_list_OPA.append(value)
            print(frame_list_OPA)
    else:
        if value in frame_list_OPA:
            print('--hit--')
        else:
            page_fault_OPA+=1
            
            for i in frame_list_OPA:
                try:
                    idx.append(tmp_ls.index(i))
                except:
                    continue    
            
            frame_list_OPA.remove(tmp_ls[max(idx)])
            frame_list_OPA.append(value)
            print(frame_list_OPA)
print('\nNumber of page fault: ', page_fault_OPA)