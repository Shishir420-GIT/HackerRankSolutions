if __name__ == '__main__':
    N = int(input())
    Data = []
    while(N>0):
        N -= 1
        com = input()
        com = com.split()
        
        if com[0] == 'insert':
            Data.insert(int(com[1]),int(com[2]))
        
        elif com[0] == 'print':
            print(Data)
        
        elif com[0] == 'remove':
            Data.remove(int(com[1]))
            
        elif com[0] == 'append':
            Data.append(int(com[1]))
            
        elif com[0] == 'sort':
            Data.sort()
            
        elif com[0] == 'pop':
            Data.pop()
            
        elif com[0] == 'reverse':
            Data.reverse()
            