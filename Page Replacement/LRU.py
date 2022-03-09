frame = int(input('Frame size: '))
referenceSTR = list(map(int, input('Reference String: ').split(',')))

frame_list_LRU = []
page_fault_LRU = 0

for value in referenceSTR: 
  
    if value in frame_list_LRU: 
        print('--hit--')
        frame_list_LRU.remove(value) 
  
        frame_list_LRU.append(value) 
  
    else: 
        if(len(frame_list_LRU) == frame): 
            frame_list_LRU.remove(frame_list_LRU[0]) 
            frame_list_LRU.append(value) 
  
        else: 
            frame_list_LRU.append(value) 
  
        print(frame_list_LRU)
        page_fault_LRU +=1
          

print('\nNumber of page fault: ', page_fault_LRU)