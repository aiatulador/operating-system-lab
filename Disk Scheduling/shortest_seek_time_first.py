queue = list(map(int, input('Enter Queue : ').split(',')))
header = int(input('Head Starts : '))

sstf = queue
path = [header]
cnt = len(sstf)-1
distance = 0
while sstf:
    
    if cnt == 0:
        sstf.remove(header)
        hdr = path[len(path)-1]
        minDist = 10**19
        for i in sstf:
            if minDist>abs(hdr-i):
                minDist = abs(hdr-i)
                temp = i
        print('({}-{})'.format(hdr,temp))
        path.append(temp)
        header=temp
    else:
        sstf.remove(header)
        hdr = path[len(path)-1]
        minDist = 10**19
        for i in sstf:
            if minDist>abs(hdr-i):
                minDist = abs(hdr-i)
                temp = i
        print('({}-{})'.format(hdr,temp),end='+')
        distance +=abs(hdr-temp)
        path.append(temp)
        header=temp

        
    cnt-=1

print('\nPath: ',path[:-1])
print('\nTotal distance:',distance," cylinders")