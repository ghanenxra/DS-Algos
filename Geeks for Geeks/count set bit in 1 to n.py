class Solution:
    def countSetBits(self,n):
        total_bits = 0
        i = 0
    
   
        while (1 << i) <= n:
            cycle_length = 1 << (i + 1)
            complete_cycles = (n + 1) // cycle_length
            total_bits += complete_cycles * (1 << i)
        
            leftover = (n + 1) % cycle_length
        
            if leftover > (1 << i):
                total_bits += leftover - (1 << i)
            i += 1
        return total_bits
     