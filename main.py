"""

17.07.23 darsdagi uyga-vazifa

4 ta masala bor

"""

#   1 - misol  ( 367 - misol )

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num < 17:
            for i in range(1, num/2 + 1):
                if i * i == num:
                    return True
        elif 17 < num <=100:
            for i in range(4, num/4):
                if i * i == num:
                    return True
        elif 100 < num <=1000:
            for i in range(10, num/10):
                if i * i == num:
                    return True
        elif 1000 < num <= 10000:
            for i in range(30, num/30+1):
                if i * i == num:
                    return True
        elif 10000 < num:
            for i in range(100, num/100):
                if i * i == num:
                    return True

        return False


#   2 - misol  ( 374 - misol)



class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = n + 1
        m = 1
        while True:

            if (n - m) <= 2:
                for i in range(m, n):
                    if guess(i) == 0:
                        return i

            if guess((n + m) // 2) == 0:
                return ((n + m) // 2)

            elif guess((n + m) // 2) == -1:
                n = ((n + m) // 2)

            elif guess((n + m) // 2) == 1:
                m = ((n + m) // 2)



#   3 - misol   (383 - misol)

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        list_q = list(ransomNote)
        list_m = list(magazine)

        for i in list_q:
            if i in list_m:
                list_m.remove(i)
            else:
                return False
        return True



#   4 - misol   (387 - misol)


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        harf_s = {}

        for harf in s:
            harf_s[harf] = harf_s.get(harf, 0) + 1

        for i in range(len(s)):
            if harf_s[s[i]] == 1:
                return i

        return -1
