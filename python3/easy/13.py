class Solution:
    def romanToInt(self, s: str) -> int:
        x = []
        for i in s:
            if i == 'I':
                x.append(1)
            elif i == 'V':
                x.append(5)
            elif i == 'X':
                x.append(10)
            elif i == 'L':
                x.append(50)
            elif i == 'C':
                x.append(100)
            elif i == 'D':
                x.append(500)
            elif i == 'M':
                x.append(1000)
        v = x[::-1]
        y = len(v)
        for i in range(y-1):
            if v[i+1] < v[i]:
                v = v*-1
        return sum(v)