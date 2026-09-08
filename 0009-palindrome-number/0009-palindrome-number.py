
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False

        result=0
        num=x
        while num>0:
          ld=num%10
          result=(result*10)+ld
          num=num//10
        return result==x
          
        
        