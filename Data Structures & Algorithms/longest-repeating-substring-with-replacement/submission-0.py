class Solution:
    def characterReplacement(self,s,k):
        count={}
        left=0
        answer=0

        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_count=max(count.values())
            
            while(right-left+1)-max_count>k:
                count[s[left]]-=1
                left+=1
                max_count=max(count.values())
            answer=max(answer,right-left+1)
        return answer
        