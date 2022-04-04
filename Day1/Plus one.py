class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(map(str,digits))
        tmp=int(s)+1
        tmmp=str(tmp)
        l=[]
        for i in tmmp:
            l.append(i)
        return l
        
