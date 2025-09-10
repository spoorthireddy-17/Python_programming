days=int(input('enter number of days:'))
registers=[]
for i in range(days):
    n=int(input(f'enter number of registrations on day{i}:'))
    emails=[]
    for j in range(n):
        mail=input()
        emails.append(mail)
    registers.append(emails)
print(registers)
    
#normalize and remove duplicates
normalized=[]
for emails in registers:
    normal=[]
    for mail in emails:
        mail_normalized=mail.lower()
        normal.append(mail_normalized)
    normalized.append(normal)
print(normalized)
unique=[]
for emails in normalized:
    uni=[]
    for mail in emails:
        if mail not in uni:
            uni.append(mail)
    unique.append(uni)
print(unique)