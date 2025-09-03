#to check alphabet or not


def alphabet(ch):
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z') ):
        return f"{ch} is a alphabet"
    else:
        return f"{ch} is not a alphabet"
cha=input('enter a character:')
res=alphabet(cha)
print(res)