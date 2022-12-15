class Solution:
    def BalancedString(self,N):
        s=sum(list(map(int,str(N))))
        alpha='abcdefghijklmnopqrstuvwxyz'
        res=''
        while N>26:
            res=res+alpha
            N=N-26
        if N<=26:
            if N%2==0:
                res=res+alpha[0:N//2]+alpha[26-N//2:]
            else:
                if s%2==0:
                    res=res+alpha[0:((N+1)//2)]+alpha[26-((N-1)//2):]
                else:
                    res=res+alpha[0:((N-1)//2)]+alpha[26-((N+1)//2):]
        return res
