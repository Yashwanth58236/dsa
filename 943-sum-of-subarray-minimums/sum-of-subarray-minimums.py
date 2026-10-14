class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        stack = []
        MOD = 10**9 + 7
        result = 0

        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                left_count = mid - left
                right_count = right - mid

                result += arr[mid] * left_count * right_count

            stack.append(i)

        return result % MOD