
class Solution:
    def countAndSay(self, n: int) -> str:
        
        f = "1"
        
        if n == 1:
            
            return f
        
        else:
            
            f = "11"
            
            for _ in range(2, n):
                                    
                z = ""
                
                a = 0
                
                b = 1
                
                while b <= len(f) - 1:
                    
                    if f[a] == f[b]:
                        
                        b = b + 1
                        
                    else:
                                            
                        z = z + str(b - a) + str(f[a])
                        
                        a = b
                        
                        b = b + 1
                        
                    if b == len(f) :

                        z = z + str(b - a) + str(f[a])
                
                f = z
                        
        return f
                    