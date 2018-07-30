with open("list.txt","r") as f:
    for line in f:
        data=line.split()
        print('{:<20},{:<15},{0[-8]:<10},{0[-7]:<10},{0[-6]:<10},{0[-5]:<10},{0[-4]:<10},{0[-3]:<10},{0[-2]:<10},{0[-1]:<10}'.format(data))