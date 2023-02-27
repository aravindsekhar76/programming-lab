a=input("Enter Elements of A : ")
a=a.split(" ")
c=[]
for i in a:
	c.append(int(i))
print("List A = ",c)

b=input("Enter Elements of B : ")
b=b.split(" ")
d=[]
for i in b:
	d.append(int(i))
print("List B = ",d)

flag=0
for i in c:
	for j in d:
		if i==j:
			flag=flag+1
			print(i ," present in both lists")
			
if flag==0:
	print("No Common Elements")
