class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            alive = True

            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop()

                elif abs(stack[-1]) == abs(a):
                    stack.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break

            if alive:
                stack.append(a)

        return stack