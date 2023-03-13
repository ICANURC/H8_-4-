age = input("enter your age:  ")
if int(age) + 365 > 20000:
    print("Time to retire!")
elif int(age) + 365 > 10000:
    print("Lots of time left!")
else:
    print("Time to get started!")