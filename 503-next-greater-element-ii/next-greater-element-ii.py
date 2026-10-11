
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        nxt = [-1] * n

        for i in range(2 * n):
            x = nums[i % n]

            while stack and nums[stack[-1]] < x:
                idx = stack.pop()
                nxt[idx] = x

            if i < n:
                stack.append(i)

        return nxt
