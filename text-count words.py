f=open("krishtext.txt","r")
s=f.read()
l=s.split()
wordcount=0
for i in l:
wordcount+=1
print(wordcount)
f.close()
