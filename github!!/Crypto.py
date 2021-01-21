data='label'
flag=''
for d in data:
    flag+=chr(ord(d) ^ 13)

print(flag)
