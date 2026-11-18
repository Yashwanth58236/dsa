
class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(index, path, total):

            if total == target:
                res.append(path[:])
                return

            if index == len(candidates) or total > target:
                return

            # Pick the current element
            path.append(candidates[index])
            backtrack(index, path, total + candidates[index])

            # Backtrack
            path.pop()

            # Skip the current element
            backtrack(index + 1, path, total)

        backtrack(0, [], 0)
        return res
