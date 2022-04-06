class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tmp=[]
        
        for i in range(numRows):
            tmp.append([0]*(i+1))
            for j in range(i+1):
                if j==0 or j==i:
                    tmp[i][j]=1
                else:
                    tmp[i][j]=tmp[i-1][j]+tmp[i-1][j-1]
        return tmp     
        
        
        
