#to print all ascii characters

def display_ascii():
    for i in range(0,255):
        print(f"{i}-> {chr(i)}", end="|")
display_ascii()