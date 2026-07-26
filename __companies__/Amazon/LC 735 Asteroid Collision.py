class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []

        def collideRet(a,b):
            if abs(a) > abs(b):
                return a
            if abs(b) > abs(a):
                return b
            return 0

        for a in asteroids:
            if a >= 0:
                ret.append(a)
                continue

            while a < 0 and ret and ret[-1] > 0:                
                a = collideRet(a, ret.pop())

            if a != 0:
                ret.append(a)                            

        return ret