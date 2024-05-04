my_list=input().split()
mayda=-9999999
for i in my_list:
    if int(i)<int(mayda) and int(i)%2!=0:
        mayda=i
print(mayda)