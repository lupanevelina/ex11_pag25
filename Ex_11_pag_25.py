n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
if n<10:
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
print(a)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[:5])

print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
print(a[::-1])

print('c)  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)


print('d)  afişează pe ecran doar componentele pare;')
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print(c)

print('e)  afişează pe ecran media aritmetică a componentelor pare;')
media=sum(c)/len(c)
print(media)

print('f)  afişează pe ecran doar componentele impare;')
l=[]
for element in range(0,len(a)):
    if a[element]%2!=0 :
        z=a[element]
        l.extend([z])
print(l)   

print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=2
y=3
m=[]
for g in range(0,len(a)) :
    if a[g]>x and a[g]%y!=0 :
        n=a[g]
        m.extend([n])
print(m)        

print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x=2
y=7
h=[]
for k in range(0,len(a)) :
    if a[k]>x and a[k]<y :
        p=a[k]
        h.extend([p])
print(h)

print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
ab=[]
for i in range(0,len(a)):
    if (a[i]%2!=0 and a[i]<0):
        ab.append(i)
print(ab)
        
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
j=[]
for el in range(0,len(a)):
    if (a[el]>9 and a[el]<100) or (a[el]<-9 and a[el]>-100):
        j.append(el)
print(j)

print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
w=a
w[0]=min(w)
print(w)

print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
f=a
y=min(f)
f[f.index(y)]=f[0]
print(f)
 

print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
r=[]
for t in range(0,len(a)):
    if a[t]%2==0:
        j=a[t]
        r.extend([j])
print(r)


print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;') 
na=[]
for v in range(0,len(a)) :
    if a[v]%3==0 :
        h=a[v]
        na.extend([h])
print(na)


print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')          
