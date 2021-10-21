def bubbleSort( arr ):         # function bubbleSort that accepts a parameter arr
    n = len( arr )

    for i in range( n - 1 ) :
        flag = 0                # used to determine if a swap has occurred or not

        for j in range(n - 1) :

            #Uses the if statement to check if the value on the left-hand side is greater than the one on the immediate right side.
            if arr[j] > arr[j + 1] :   
                tmp = arr[j]
                arr[j] = arr[j + 1]
               arr[j + 1] = tmp
                flag = 1         #The flag variable is assigned the value 1 to indicate that a swap has taken place

        if flag == 0:
            break

    return arr

ar = [5,3,8,6,7,2] 

result = bubbleSort(ar)

print (result)