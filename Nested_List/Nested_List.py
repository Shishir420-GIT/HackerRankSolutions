if __name__ == '__main__':
    student_data = []
    for _ in range(int(input())):
        student=[]
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        student_data.append(student)

    #student_data = [['harry', 30.0], ['barry', 30.0], ['Marry', 29.0], ['carry', 41.0], ['larry', 35.0]]

    def get_lowest(data):
        lowest = data[0][1]
        for i in data:
            if lowest > i[1]:
                lowest = i[1]
        return lowest

    def remove_element(data,value):
        temp = []
        for j in data:
            if not value == j[1]:
                temp.append(j)
        return temp

    def sort_names(data,value):
        names = []
        for j in data:
            if value == j[1]:
                names.append(j[0])
        return sorted(names)

    lowest = get_lowest(student_data)

    temp_data = remove_element(student_data,lowest)

    sec_lowest = get_lowest(temp_data)

    sorted_names = sort_names(student_data,sec_lowest)

    print(sorted_names)