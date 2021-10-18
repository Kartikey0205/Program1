def bubble_sort(lst):
    flag = True

    while flag :
        flag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                flag = True


lst = [1,5,2,7]

bubble_sort(lst)
print(lst)
