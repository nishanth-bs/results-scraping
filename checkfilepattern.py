pattern = input("enter")
with open ("dataasneededfinal.txt","rt") as file:
    for lineno, line in enumerate(file):
        if pattern in line:
            print(line)