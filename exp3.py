print("Enter details of contigency table of nominal data:")
x=int(input("\nEnter the no. of rows in contigency table:"))
y=int(input("\nEnter the no. of attributes in contigency table:"))
print("\nEnter the elements in contigency table:")
num=[]
b=0
tb=[0 for i in range(y)]
for i in range(x):
 r=[]
 tv=0
 for j in range(y):
  a=int(input())
  tv=tv+a
  r.append(a)
  tb[j]=tb[j]+a
 r.append(tv)
 b=b+tv
 num.append(r)
tb.append(b)
num.append(tb)
x2=0
print("\nEntered data:")
for i in range(x+1):
 for j in range(y+1):
  print(num[i][j],end=" ")
  if(i<x and j<y):
     c=((num[x][j]*num[i][y])/num[x][y])
     x2=x2+(((num[i][j]-c)**2)/c)
 print()
print("\nX2 of given data:",x2) 
if(x2>10.828):
 print("\nReject the hypothesis")
else:
 print("\nAccept the hypothesis")
print("\nEnter the details of 2D data set of Numeric data:")
g=int(input("\nEnter the no. of data sets in 2D data set:"))
xm1=0
xm2=0
xd=[]
for i in range(g):
 r="X"+str(i+1)+":"
 a=input(r).split(" ")
 xd.append(a)
 xm1=xm1+float(a[0])
 xm2=xm2+float(a[1])
 xd.append(a)
xm1=xm1/g
xm2=xm2/g
q=0
v1=0
v2=0
for i in range(g):
 q=q+((float(xd[i][0])-xm1)*(float(xd[i][1])-xm2))
 v1=v1+((float(xd[i][0])-xm1)**2)
 v2=v2+((float(xd[i][1])-xm2)**2)

v1=(v1/g)**0.5
v2=(v2/g)**0.5
print("Rab of numeric data:",round((q/(g*v1*v2)),3)) 
if((q/(g*v1*v2))>0):
 print("Positive Correlation")
elif((q/(g*v1*v2))==0):
 print("\nNo Correlation")
else:
 print("\nNegative Correlation")

