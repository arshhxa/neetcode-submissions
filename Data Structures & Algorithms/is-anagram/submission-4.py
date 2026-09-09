class Solution:
    def isAnagram(self,s,t):
        count1={}
        count2={}
        if len(s)!=len(t):
            return False
        for char in s:
            count1[char]=count1.get(char,0)+1
        for char in t:
            count2[char]=count2.get(char,0)+1
        return count1==count2
    

        