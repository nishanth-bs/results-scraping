import re
choice=input('Enter the pattern to find the results of all names starting with it')
with open('dataasneededfinal.txt','rt') as file_in:
    for line in (file_in):
       # if line.find("e"):checkfilepattern.py:5
        string=line[0]
        if(((string.find(choice,0)) is not -1)):
                print(line)
"""
        while pointer<(str1):
            pointer = str.find(b,choice, pointer)
            if pointer is -1:
                break
            print("Result:\nusn:1RN15"+str[:5])
            pointer+=len(choice)

            pointer = 0
            string = line
            pointer = string.find(choice)
            if pointer is not -1:
                print("Name:", "USN:1RN15", str(line[:5]))
            print(1)
            continue
"""