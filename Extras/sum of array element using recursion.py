def sum_arr(arr,start ,end):
    if start == end:
        return arr[start]
    
    return arr[start] + sum_arr(arr,start+1,end)

print(sum_arr([1, 2, 3, 4, 5,6 , 7,8 ,9 ],0,8))