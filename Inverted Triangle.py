#PROBLEM = INVERTED TRIANGLE
num=int(input("Enter the number of rows: "))
for i in range(num,0,-1):
    for e in range(0,num-1):
        print(end="")
        for e in range(0,i):
            
            print("*", end="")
        print()
