import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse N and frequencies
    N = int(input_data[0])
    frequencies = []
    idx = 1
    for _ in range(N):
        frequencies.append(int(input_data[idx]))
        idx += 1

    # Parse K and keySizes
    K = int(input_data[idx])
    idx += 1
    key_sizes = []
    for _ in range(K):
        key_sizes.append(int(input_data[idx]))
        idx += 1

    # 1. Check if all letters can fit on the keypad
    if sum(key_sizes) < N:
        print(-1)
        return

    # 2. Sort frequencies in descending order
    frequencies.sort(reverse=True)

    total_keystrokes = 0
    current_press_count = 1  # Start with 1 keystroke required
    freq_idx = 0

    # 3. Fill positions level by level (1st press, 2nd press, etc.)
    while freq_idx < N:
        keys_used_this_level = 0
        
        for i in range(K):
            if freq_idx >= N:
                break
            
            # If the current key still has room at this depth level
            if key_sizes[i] >= current_press_count:
                total_keystrokes += frequencies[freq_idx] * current_press_count
                freq_idx += 1
                keys_used_this_level += 1
        
        # Move to the next keystroke depth level (e.g., 2 taps, 3 taps...)
        current_press_count += 1

    print(total_keystrokes)

if __name__ == '__main__':
    solve()