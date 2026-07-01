class Solution:
    def getMinMax(self,arr):

        Min_no = arr[0]
        Mxn_no = arr[0]


        for nums in arr:
            if nums > Min_no:
                Min_no = nums

            if nums < Mxn_no:
                Max_no = nums

        
        return [Min_no , Max_no]