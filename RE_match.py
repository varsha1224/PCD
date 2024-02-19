# CHECK IF A STRING IS ACCEPTED BY RE

def union():
    a=var.pop()
    b=var.pop()
    l=[]
    l.extend(b)
    l.extend(a)
    var.append(l)
def concatenation():
    a=var.pop()
    b=var.pop()
    c=[]
    for i in range(len(b)):
        for j in range(len(a)):
            c.append(b[i]+a[j])
    var.append(c)
def closure():
    a=var.pop()
    b=''.join(a)
    c=b[::-1]
    res=[]
    for i in range(len(a)):
        t=[]
        for k in range(10):
            t.append(a[i]*k)
        res.extend(t)
    t1=[]
    for k in range(10):
        t1.append(b*k)
    t2=[]
    for k in range(10):
        t2.append(c*k)
    res.extend(t1)
    res.extend(t2)
    var.append(res)

from collections import deque
import re
from itertools import product

print("Enter the regular expression with appropriate brackets !! ")
rg=input("Enter the reg expression :- ")
oper=deque()
var=deque()
pattern = r'^[a-zA-Z0-9]+$' 
match = re.match(pattern, string)

if match:
	print("Matched")
else:
	print("Not")
 
for i in range(len(rg)):
    if rg[i]=='(':
        oper.append(rg[i])
    elif rg[i].isalpha()==True:
        var.append(list(rg[i]))
    elif rg[i] in '+.*':
        oper.append(rg[i])
    elif rg[i]==')':
        t=[]
        while oper[-1]!='(':
           t.append(oper.pop())
        oper.pop()
        if len(t)%2==1:
            if t[0]=='+':
                union()
            elif t[0]=='.':
                concatenation()
            elif t[0]=='*':
                closure()          
        else:
            if t[0]=='*':
                closure()
                if t[1]=='+':
                    union()
                if t[1]=='.':
                    concatenation()
            elif t[1]=='*':
                closure()
                if t[0]=='+':
                    union()
                if t[0]=='.':
                    concatenation()
result=[]
for i in var:
    result.extend(i)
result=list(set(result))
result.sort()
print(result)
