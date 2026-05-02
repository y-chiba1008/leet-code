class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        work = x
        reverse = 0
        while work > 0:
            reverse = reverse * 10 + work % 10
            work = work // 10

        return reverse == x
