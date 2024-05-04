my_list=input().split()
cnt=0
for i in  my_list:
    for j in my_list:
        if i==j:
            cnt+=int(i)
        if cnt<2:
            print(i)