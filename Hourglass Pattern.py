#Hourglass Pattern using '*' in Python

rows = int(input("Enter the desired number of rows: "))  
k = rows - 2  

# This will print the downward directed pyramid  

for i in range(rows, -1 , -1):  
    for j in range(k , 0 , -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i+1):  
        print("* " , end="")  
    print()  
  
# This will print the upward directed pyramid  

k = 2 * rows  - 2  
for i in range(0 , rows+1):  
    for j in range(0 , k):  
        print(end="")  
    k = k - 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print()  