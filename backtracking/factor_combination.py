
#question-> expalin how a string of 2 is formed, vs a string greated than 2 e.g 3 & 4
#explain a case of no/null for  result
#
class Solution:
    def getFactors(self,n):
    
       result=[]
       curr_comb=[]
       self.backtrack_factor_check (n,2,curr_comb,result)
       
       return result       
       
    def backtrack_factor_check (n,start,curr_comb,result)
       #exit conditions 
       if n%start!=0 or if start>=n:
        return False
        
       #success conditions
       if n%product==0:
        return True     
         
       
       
       
       for num in range(start,int(sqrt(n+1))+1):
           if n%num==0:
            curr_comb.append(num)
            result.append(list(curr+ [n//num])  
            
            self.backtrack_factor_check(n//num,curr_comb,result)
            curr.pop()
            
       return result
       
              
           
           #append some how
           #if not back track
           
        
                   
        
    
       
       #recursive function
       
       #pseudocode:
       #write a backtracking recursive function that checks for products
       #sequentially builds up from modulo
       #append success items
       #take into consideration lists
       # can't see why i need a start point yet...
       

