class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        xor = 0

        for i in range(N):
            xor = xor ^ A[i]

        # print((xor>>1)&1)

        # temp=xor
        pos = 0
        i = 0
        while xor > 0:
            # print(i,xor)
            if xor & 1 == 1:
                # print('xor1',xor&1)
                pos = i
                break
            i += 1
            xor = xor >> 1
        # print(pos)

        ans = [0, 0]
        i = 0
        while i < N:
            if A[i] & (1 << pos) != 0:
                ans[1] = ans[1] ^ A[i]
            else:
                ans[0] = ans[0] ^ A[i]
            i += 1
        if ans[1] < ans[0]:
            temp = ans[1]
            ans[1] = ans[0]
            ans[0] = temp
        return ans  


