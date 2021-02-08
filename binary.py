import pickle
student=[]
f=open('student.dat','wb')
ans='y'
while ans.lower()=='y':
    roll=int(input('enter roll number:'))
    name=input('enter name:')
    student.append([roll,name])
    ans=input('add more?(y)')
pickle.dump(student,f)
f.close
f=open('student.dat','rb')
student=[]
while True:
    try:
        student=pickle.load(f)
    except EOFError:
        break
ans='y'
while ans.lower()=='y':
    found=False
    r=int(input('enter roll number to serach:'))
    for s in student:
        if s[0]==r:
            print('##name is ',s[1],'##')
            found=True
            break
    if not found:
        print('###Sorry! roll number not found###')
    ans=input('search more?(y):')
f.close()
            
            
    
        
