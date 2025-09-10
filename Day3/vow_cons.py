def check(str):
    vow=0
    cons=0
    for s in str:
        if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u'or s=='A' or s=='E' or s=='I' or s=='O' or s=='U'):
            vow+=1
        else:
            cons+=1
    print(f"{vow} vowels and {cons} consonants in {str}")
str=input('enter string:')
check(str)