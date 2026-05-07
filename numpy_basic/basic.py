import numpy as np 

a=np.array([1,2,3,4])
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b)

print(a.ndim)#tells the dimension of the array 

print(a.shape)
print(b.shape)#tells the no of rows and no column etc

print(a.dtype)#print the type
print(b.dtype)

print(a.itemsize)#give the size


c=np.array([[1,2,3,4,5,6,7],[7,8,5,4,3,2,6]])
print(c.shape)
print(c[1,4])#accessing a particular element in the array

print(c[1:])#accessing a particular row

print(c[:,6])#accessing a particular column


print(c[0,1:6:2])#accessing a sub array


d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d)
print(d.ndim)
print(d.shape)
print(d[1,0,1])#first get the layer then row and column


#all zero matrix
print(np.zeros((3,3,4)))

#all ones matrix
print(np.ones((4,2)))

#all any number
print(np.full((2,2),56))

#full_like
print(np.full(a.shape,44))
print(np.full_like(a,44)) #both will give the same output 


#matrix of the random decimal number 
print(np.random.rand(2,4))
print(np.random.random_sample(a.shape))

#for integer
print(np.random.randint(5,size=(3,3)))

#for indetity matrix
print(np.identity(3))


arr=np.array([[1,2,3]])
r1=np.repeat(arr,3) #without the axis it repeat in array
print(r1)
#axis=0
r2=np.repeat(arr,2,axis=0)
print(r2)



output=np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9
output[1:4,1:4]=z
print(output)

#copy
a=np.array([1,2,3,4])
b=a.copy()
b[0]=2
print(b)
print(a)

#airthmetic
ar=np.array([1,2,3,4])
ar=ar+2
ar=ar-2
print(ar)


##linear algebra
hb=np.full((3,3),7)
print(hb)
bh=np.full((3,3),5)
print(bh)
print(np.matmul(hb,bh))

#determinant
k=np.identity(3)
k=k*5
print(np.linalg.det(k))


#statistics
stats=np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats))
print(np.min(stats,axis=0))#column wise
print(np.max(stats,axis=1))#row wise

print(np.sum(stats))
print(np.sum(stats,axis=0))#column wise 
print(np.sum(stats,axis=1))#row wise 

#reorgenizing the array
before=np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after=before.reshape((4,2))
print(after)

#stacking the array
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2]))#this will stack them vertically
h1=np.full((2,2),4)
h2=np.full((2,2),7)
print(np.hstack((h1,h2)))

#boolean masking and advance indexing 
a=np.array([1,2,3,4,5,6,7,8,9])

print(a[[0,2,8]])


prac=np.ones((6,5))
print(prac)
print(prac[2:4,0:2])