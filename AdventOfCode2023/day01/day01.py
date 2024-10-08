sum = 0
with open('./AdventOfCode2023/day01/input.txt','r') as f:
    for line in f:
        i = 0
        while i <= len(line):
            if line[i].isnumeric():
                sum += int(line[i])
                break
            i += 1
        j = len(line) - 1
        while j >= 0:
            if line[j].isnumeric():
                sum += int(line[j])
                break
            j -= 1     
 #   print(line, end='')
print(sum)