"""

12.07.23 darsdagi uyga-vazifa

3 - masala bor

"""

#   1 - misol

################

#   2 - misol

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        list1 = []
        for i in range(20):
            if n == 3 ** i:
                return True
        return False


#   3 - misol

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        list1 = [0]
        for i in range(1, n + 1):
            binary = ''
            while i > 0:
                binary = str(i % 2) + binary
                i = i // 2
            son = 0
            for j in binary:
                son += int(j)
            list1.append(son)
        return list1


