'''
        Input: secret = "1807", guess = "7810"
        Output: "1A3B"
'''
from collections import Counter
import operator
guess='7810'
secret="1807"

a=b=0
ans=[]
g=[]
s=[]
n=len(guess)
g=list(guess)
s=list(secret)
        
for i in range(n):
    if(guess[i]==secret[i]):
        del g[i]
        del s[i]
        g.insert(i,'a')
        s.insert(i,'Z')
        a+=1
    
for i in range(n):
    if(g[i] in s):
        s.remove(g[i])
        b+=1
print(f"{a}A{b}B")

"""
        another Method
"""
#this will see how many are matching secret with guess
#like 1807 ---> 7810
#number 8 is common so sum(matches)==1
#a = 1
a=sum(map(operator.eq,secret,guess))
#print(a)
b=0
#key value pair
g=Counter(guess)

s=Counter(secret)

for key in g.keys():
    b+=min(s.get(key,0),g.get(key,0))
        
print(f'{a}A{b-a}B')