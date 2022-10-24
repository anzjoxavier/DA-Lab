from itertools import combinations
def checks(n,a):
  t=0
  for i in n:
    f=0
    for j in a:
      if(j not in i):
        f=1
    if(f==0):
      t=t+1
  return t

def sub_lists (l):
    comb = []
    for i in range(len(l)+1):
        comb += [list(j) for j in combinations(l,i)]
    return comb
    
a=int(input("Enter the no. of transactions:"))
b=int(input("Enter the no. of itemset:"))
s=[]
g=[ "I"+str(i+1) for i in range(b) ]
print("Enter itemset of each transaction seaperated by space:")
s=[]
for i in range(a):
 x=input("T_"+str((i+1)*100)+":")
 f=x.split(" ")
 f.sort()
 s.append(f)
print("\nEntered data:")
for i in range(a):
 print("T_"+str((i+1)*100)+":",end=" ")
 for j in s[i]:
   print(j,end=" ")
 print()

for i in range(1,b+1):
 print("L"+str(i)+":")
 O=0
 for j in sub_lists (g):
   if(len(j)==i):
      if(checks(s,j)>=2):
        O=1 
        print(j,":",checks(s,j))
 if(O==0):
    print("No items") 

 
