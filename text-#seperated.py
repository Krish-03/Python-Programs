f=open("aruntext.txt","r")
s=f.readline()
for i in s.split():
    print(i,end="#")
f.close()
