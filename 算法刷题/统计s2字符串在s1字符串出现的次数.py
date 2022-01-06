class Solution:
    def subsstr_count(self, s1, s2):
        m = len(s1)
        n = len(s2)
        res = 0
        for i in range(m - n + 1):
            if s1[i:i + n] == s2:
                res += 1
        return res


if __name__ == '__main__':
    s1 = 'ABOCABD'
    s2 = 'AB'
    print(Solution().subsstr_count(s1, s2))
