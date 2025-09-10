str_input = input('Enter a string: ')
visited = []
freq_list = []
for s in str_input:
    if s not in visited :
        count = 0
        for char in str_input:
            if s == char:
                count += 1
        freq_list.append((s, count)) 
        visited.append(s)

max_freq = freq_list[0][1]
max_char = freq_list[0][0]

for ch, count in freq_list:
    if count > max_freq:
        max_freq = count
        max_char = ch

print(f"Highest frequency character: {max_char}{max_freq}")
