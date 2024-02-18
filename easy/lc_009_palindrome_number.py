class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Base Case(s):
        ###################################################################
        # Negative numbers will never be a palindrome
        if x < 0:
            return False
          
        # String Approach:
        ###################################################################
        # Time:
        # Conversion to str ~ O(n) While Loop => O(n / 2) => O(n)
        # Space => O(1)

        # x_str = str(x)
        
        # l = 0
        # r = len(x_str) - 1
        
        # while l < r:
        #     if x_str[l] != x_str[r]:
        #         return False

        #     l += 1
        #     r -= 1
        
        # return True
        ###################################################################

        # Integer Division Approach:
        ###################################################################
        # Time => O(n) Space => O(1)
        reversed_x = self._reverse_int(x)
        return reversed_x == x
        ###################################################################

    def _reverse_int(self, x: int) -> int:
        temp = x
        reverse = 0
        while temp > 0:
            rem = temp % 10

            reverse = int(reverse * 10 + rem)

            temp = int(temp / 10)

        return reverse
