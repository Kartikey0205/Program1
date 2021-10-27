
def find_max_subarray(alist, start, end):
    '''Kadane’s algorithm is an iterative dynamic programming algorithm in which we search for a maximum sum contiguous subarray within a one-dimensional numeric array.'''
    
    arr = []
    max_ending_at_i = max_seen_so_far = alist[start]
    max_left_so_far = start
    fin_max_far, prev_max_left = 0, 0
    max_right_so_far = 0
    if max_ending_at_i < 0:
        prev=1
        max_ending_at_i=0
    else:
        prev=0
    for i in range(start + 1, end):
        x=alist[i]
        max_ending_at_i += alist[i]

        if max_ending_at_i > max_seen_so_far:
            max_seen_so_far = max_ending_at_i
            if i == end-1 and max_seen_so_far > fin_max_far:
                fin_max_far = max_seen_so_far
                arr.append(max_seen_so_far)
                max_right_so_far = i
                max_left_so_far = prev
                prev = i+1
        else:
            if max_seen_so_far > fin_max_far:
                fin_max_far = max_seen_so_far
                max_right_so_far = i-1
                max_left_so_far = prev
                prev = i+1
            next=i+1
            arr.append(max_seen_so_far)
            max_ending_at_i,max_seen_so_far = 0,0
    return max_left_so_far, max_right_so_far, max(arr)

alist = [5, -1, 5, 4, 4, 5, 4, 10, -5, 2, 1, 3, 5, 10, 1]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end, maximum))
