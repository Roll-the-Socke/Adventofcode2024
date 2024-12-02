

def checkReport(data):
    decreasing = False
    increasing = False
    for index in range(len(data) - 1):
        diff = data[index] - data[index+1]
        if diff > 0:
            increasing = diff > 0
        if diff < 0:
            decreasing = diff < 0  
        if increasing and decreasing or not (0 < abs(diff) < 4):
            return False
    return True

with open("input1.txt") as input:
        safe = 0
        for line in input:
            row = line.rstrip()
            row = list(map(int, row.split()))
            if checkReport(row):
                safe += 1

        print("\npart 1: ",safe)


with open("input1.txt") as input:
        safe = 0
        for line in input:
            row = line.rstrip()
            row = list(map(int, row.split()))

            check = checkReport(row)

            if not check:
                for i in range(len(row)):
                    temp = row.pop(i)
                    check = checkReport(row)
                    if check:
                        break
                    row.insert(i, temp)
            if check:
                safe += 1
        print("\npart 2: ",safe)