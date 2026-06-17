class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        # Iterate through all 32 bits of an integer
        for i in range(32):
            bit_count = 0
            for num in nums:
                
                bit_count += (num >> i) & 1
            
            if bit_count % 3 != 0:
              
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
                    
        return ans