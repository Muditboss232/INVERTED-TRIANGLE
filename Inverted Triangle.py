#PROBLEM = INVERTED TRIANGLE
num=int(input('Enter an odd number width: '))
for i in range(num+1, 0, -1) :
    number = int((num - i)/2)
    print(' '* number + '*'*i)