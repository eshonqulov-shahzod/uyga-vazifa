"""

14.07.23 darsdagi uyga-vazifa

4 ta masala bor

"""

#   1 - misol  ( 292 - misol )

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 != 0:
            return True
        else:
            return False


#   2 - misol  ( 342 - misol)

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        for i in range(16):
            if pow(4, i) == n:
                return True
        return False



#   3 - misol   (344 - misol)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n1 = 0
        n2 = len(s) -1

        while n1 < n2:
            s[n1], s[n2] = s[n2], s[n1]
            n1 += 1
            n2 -= 1
        return s



#   4 - misol   (345 - misol)


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        list1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        list2 = []

        for i in range(len(s)):
            if s[i] in list1:
                list2.append(i)

        list3 = list2[::-1]

        for i in range(len(list2) // 2):
            s[list2[i]], s[list3[i]] = s[list3[i]], s[list2[i]]

        s1 = ""
        for i in s:
            s1 += i

        return s1

