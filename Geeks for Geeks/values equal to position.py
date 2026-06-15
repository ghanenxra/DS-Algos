class Solution:
    def valEqualToPos(self, arr):
        arr_new = []
        for i in range(len(arr)):
            if arr[i] == i+1:
                # Python uses 0-based indexing, but the problem uses 1-based positions
            # so we compare arr[i] with (i+1) to match the problem's position numbering
                arr_new.append(i+1)
                # append (i+1) since the answer should be in 1-based position, not 0-based index
            else:
                pass
        return arr_new
        