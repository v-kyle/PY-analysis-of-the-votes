def pa(h):
    uu=''
    h10=h%10;
    if h10==1: uu='голос'
    elif h10>=2 and h10<=4 and (h<10 or h>20): uu='голоса'
    else: uu='голосов'
    return uu
    
f=open('ttt.txt')
b=[0]*30
t=[-1,-1,-1]
ti=[-1,-1,-1]



a=f.read().split()
for i in range(len(a)):
    a[i]=a[i][0:2]
    if a[i][1]==".": a[i]=a[i][0:1]
    
for i in range (len(a)):
    b[int(a[i])]+=1
    
for i in range(9,30):
    print("{} Января - {} {}".format(i,b[i],pa(b[i])))

for i in range(9,30):
    if int(b[i])>t1:
        t1=b[i]
        t1i=i
for i in range(9,30):
    if int(b[i])>t2 and i!=t1i:
        t2=b[i]
        t2i=i
for i in range(9,30):
    if int(b[i])>t3 and i!=t1i and i!=t2i:
        t3=b[i]
        t3i=i

        
print("")
print('Топ 3 дня, за которые проголосовали:')
for i in range(1,4):
    print('{} Января - {} {}'.format(
    {} Января - {} {}
    {} Января - {} {}
    '''.format(t1i,t1,pa(t1),t2i,t2,pa(t2),t3i,t3,pa(t3)))

      
      

    
    
    
