str_input = input('Enter a string: ')
visited = []

for s in str_input:
    if s not in visited : 
        count = 0
        for char in str_input:
            if s == char:
                count += 1
        print(f"{s}{count}",end='')
        visited.append(s)
