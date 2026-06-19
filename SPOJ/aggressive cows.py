import sys

def can_place_cows(stalls, num_cows, min_dist):
    """
    Greedy function to check if we can place 'num_cows' in 'stalls'
    such that every adjacent cow is at least 'min_dist' apart.
    """
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]  # Place next cow here
            
            if count >= num_cows:
                return True
                
    return False

def solve():
    # Read all input from standard input efficiently
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    num_test_cases = int(data[0])
    idx = 1
    
    out = []
    for _ in range(num_test_cases):
        N = int(data[idx])
        C = int(data[idx+1])
        idx += 2
        
        stalls = []
        for _ in range(N):
            stalls.append(int(data[idx]))
            idx += 1
            
        # 1. Sorting the stalls is essential for greedy placement
        stalls.sort()
        
        # 2. Binary search for the maximum minimum distance
        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_place_cows(stalls, C, mid):
                ans = mid      # 'mid' is a feasible distance, try to look for a larger one
                low = mid + 1
            else:
                high = mid - 1 # 'mid' is too large, reduce the search range
                
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()