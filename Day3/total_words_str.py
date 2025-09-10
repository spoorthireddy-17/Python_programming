text = input("Enter string: ")
count = 0
i = 0
n = len(text)
while i < n:
    while i < n and text[i] == " ":
        i += 1
    if i < n:
        count += 1
    while i < n and text[i] != " ":
        i += 1
print("Number of words:", count)
