str_input = input('Enter a string: ')
visited = []
freq_list = []

for s in str_input:
    if s not in visited:
        count = 0
        for char in str_input:
            if s == char:
                count += 1
        freq_list.append((s, count))  
        visited.append(s)

min_freq = freq_list[0][1]
min_char = freq_list[0][0]

for ch, count in freq_list:
    if count < min_freq:
        min_freq = count
        min_char = ch
print(f"Lowest frequency character: {min_char}{min_freq}")
