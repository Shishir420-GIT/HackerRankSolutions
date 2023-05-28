if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    #get the max number from the array
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]

    #remove the max number from list
    new_list = []
    for j in range(len(arr)):
        if not (arr[j] == max):
            new_list.append(arr[j])
    
    #get the max number from new list
    runner = new_list[0]
    for k in range(len(new_list)):
        if runner < new_list[k]:
            runner = new_list[k]

    print(runner)
