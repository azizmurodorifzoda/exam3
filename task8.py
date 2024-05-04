my_list=input().split()
cnt=len(my_list)
for i in my_list:
    my_list.remove(i)
    if i in my_list:
        cnt-=1
print(cnt)