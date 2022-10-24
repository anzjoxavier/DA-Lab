def display1(a):
  for i in a:
    for j in i:
       print(j,end=" ")
    print()



print("Enter the file name:")
filen=input()
f=open(filen,"r")
u,p=0,0
data=[]
for i in f.readlines():
  l=i.split()
  data.append(l)
  u=u+1
  
s=len(data[0])
print("Table in File:")
display1(data)
normat=[]
nummat=[]
for b in range(1,u):
 nor=[]
 num=[]
 for c in range(s):
   if(data[0][c]=='n'):
     nor.append(data[b][c])
   elif(data[0][c]=='o'):
     num.append(data[b][c])
 normat.append(nor)
 nummat.append(num)   
print("Norminal Table:")
display1(normat)
print("Number Table:")
display1(nummat)   
p=len(normat[0])
ind,m=0,0
d_mat=[[0 for _ in range(u-1)] for _ in range(u-1)]
for i in range(u-1):
  for j in range(i+1,u-1):
     while(ind<p):
      if(normat[i][ind]==normat[j][ind]):
        m=m+1
      ind=ind+1
     d_mat[j][i]=(p-m)/p
     m,ind=0,0
print("Dissimilarity matrix of Nominal Values:") 
display1(d_mat)
c_mat=[[0 for _ in range(u-1)] for _ in range(u-1)]
imd=0
q=len(nummat[0])
for i in range(u-1):
  for j in range(i+1,u-1):
    while(imd<q):
      c_mat[j][i]=c_mat[j][i]+((int(nummat[i][imd])-int(nummat[j][imd]))**2)
      imd=imd+1
    imd=0
    c_mat[j][i]=round((c_mat[j][i])**0.5,2)
print("Dissimilarity matrix of Numeric values:")     
display1(c_mat)

print("Enter i and j for nominal data to find similarity:")
a=int(input())
b=int(input())
if(a>b):
 print("Similarity:",(1-(d_mat[a-1][b-1])))
elif(b>a):
 print("Similarity:",(1-(d_mat[b-1][a-1])))
else:
 print("Similarity:",1)

#s=len(data[0])
#d_mat=[[0 for _ for in range(u-1)] for _ in range(u-1)]
#m,ind=0,1
#for i in range(1,u):
  
