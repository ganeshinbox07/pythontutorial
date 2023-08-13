#!/usr/bin/env python
# coding: utf-8

# In[7]:


def mat(f,s):
    a=f+s
    b=f-s
    return(a,b)
f=int(input("enter first num"))
s=int(input("enter the second num"))
a,b=mat(f,s)
print(a)
print(b)


# In[34]:


y=10
def add():
    r=15
    r=r+25
    print(r)
add()
print(y)


# In[36]:


def fun():
    return 10,11,12
print(fun())


# In[8]:


x=13
def san():
    x=12
    print(x)
san()
print(x)


# In[39]:


class a:
    def nam(ba):
        ba.na=input("enter the name")
        ba.ro=int(input("enter the rollno"))
    
class b:
    def mark(ba):
        ba.tam=int(input("enter the tam mark"))
        ba.eng=int(input("enter the eng mark"))
        
class c(a,b):
    def tot(ba):
        ba.mat=int(input("enter the mat mark"))
        ba.sci=int(input("enter the sci mark"))
        print(ba.na)
        print(ba.ro)
        print(ba.tam)
        print(ba.eng)
        print(ba.mat)
        print(ba.sci)

class d(c):
    def dis(ba):
        t=ba.tam+ba.eng+ba.mat+ba.sci
        print(t)
        
gan=d()
gan.nam()
gan.mark()
gan.tot()
gan.dis()


# In[59]:


class gan:
    def ga(ba):
        ba.name=input("enter your name ")
        ba.roll=int(input("enter roll no "))
        
class math:
    def ma(ba):
        ba.rice=int(input("enter rice packs "))
        ba.daal=int(input("enter the daal packs "))
        ba.ma=ba.rice+ba.daal
        
class mama:
    def mam(ba):
        ba.line=int(input("enter the line packs "))
        ba.unline=int(input("enter the unline packs "))
        ba.mam=ba.line+ba.unline
        
class arun(gan,math,mama):
    def ar(ba):
        print(ba.name)
        print(ba.roll)
        print(ba.rice)
        print(ba.daal)
        print(ba.line)
        print(ba.unline)
        print("total of ma",ba.ma)
        print("total of mam",ba.mam)
        
vengi=arun()
vengi.ga()
vengi.ma()
vengi.mam()
vengi.ar()


# In[3]:


from array import *

x=array("i",[])
print("enter the limit")
n=int(input())
print("enter the value")
for i in range(n):
    x.append(int(input()))
print(x)
sum(x)


# In[11]:


n=int(input("enter the input"))
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end="")
            
    print("")
   


# In[55]:


n=int(input("enter your num"))
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
        
    print("")


# In[11]:


b=int(input("enter the num"))
for i in range(b):
    for j in range(b-i):
        print("*",end="")
    print()


# In[61]:


n=int(input("enter the num"))
k=n
for i in range(0,n):
    for j in range(i):
        print(end=" ")
    for j in range(k,0,-1):
        print("*",end=" ")
    k=k-1
    print()



# In[45]:


for i in range(10,0,-2):
    print(i)


# In[63]:


n=int(input("enter the value"))
a=0
b=-1
c=1
for i in range(n):
    a=b
    b=c
    c=a+b
    print(c)


# In[71]:


n=int(input("enter the value"))
a=0
b=-1
c=1
d=0
for i in range(n):
    a=b
    b=c
    c=a+b
    print(c)
    d=d+c
print("the sum of fibonaci series",d)


# In[1]:


a=[12345]
print(a)


# In[2]:


a=[1,2,3,4,5,6]
print(a)


# In[4]:


a=['1','2','3','4']
print(a)


# In[7]:


a=['1','gan','2','mathi','arun','mama','3','4']
for i in a:
    print(i)
print(a)


# In[18]:


a=[10,20,'gan']
b=a
b+=[30,40,'mathi']
print(a)


# In[23]:


def add():
    x=5
    x+=x+4
    print(x)
add()  
x=4
print(x)


# In[10]:


x=0
while x<=18:
    x=x+3
print(x)


# In[15]:


a=1/3
b=3/1
print(a*b)


# In[16]:


1/3


# In[17]:


3/1


# In[18]:


0.3333333333333333*3.0


# In[28]:


def fun():
    return[i for i in range(0,3,3)]
print(fun())


# In[1]:


s="pythonecoder"


# In[2]:


print(s)


# In[3]:


s[1:5]


# In[18]:


s[0:8:2]


# In[14]:


s[11:0:-2]


# In[20]:


a,b,c,d=5,"gan",10.5,"10 mathi"


# In[21]:


a


# In[22]:


b


# In[23]:


c


# In[24]:


d


# In[26]:


def myfun(n):
    return lambda a:a*n
mathi=myfun(5)
print(mathi(2))


# In[25]:


tg=lambda a,b:a+b
print(tg(50,30))


# In[30]:


sr=lambda x:x**x
print(sr(5))


# In[32]:


a=5**5
a


# In[36]:


5*5*5*5*5


# In[28]:


import math
g=int(input("enter the value"))
math.factorial(g)


# In[ ]:




