#A cipher project entirely 100% by me

cipher="ruynicvbkl"
mode=13
m=""
key="gu"
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="abcdefghijklmnopqrstuvwxyz "
d="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
e="abcdefghijklmnopqrstuvwxyz0123456789"
f="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
g="abcdefghijklmnopqrstuvwxyz0123456789 "
h="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
i=" abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?:\"\'"
num="1234567890"
dec="0123456789"
q="1234567890qwertyuiopasdfghjklzxcvbnm"
qw=["1234567890","qwertyuiop","asdfghjkl","zxcvbnm"]
b64="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
morsecode={"a":"01","c":"1010","b":"1000","e":"0","d":"100","g":"110","f":"0010","i":"00","h":"0000","k":"101","j":"0111","m":"11","l":"0100","o":"111","n":"10","q":"1101","p":"0110","s":"000","r":"010","u":"001","t":"1","w":"011","v":"0001","y":"1011","x":"1001","z":"1100","1":"01111","0":"11111","3":"00011","2":"00111","5":"00000","4":"00001","7":"11000","6":"10000","9":"11110","8":"11100"}

'''
def fengjie(a,b):
  c=[]
  for i in range(b-1,int((a**0.5)+1)):
    if a%i==0:
      print i,a,c
      c.append(i)
      a/=i
      c.extend(fengjie(i-1,a))
    elif a<i:
      return c
  return c

'''

def atbash(c):
  r=""
  for i in c:
    r=r+b[25-a.find(i)]  
  return r

def morse(c,p):
CODE={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
  r=""
  for ch in c:
    for cr in str(morsecode[ch]):
      r=r+p[int(cr)]
    r=r+p[2]
  return r
  
def switch_base(number,s1,s2):
  number=str(number)
  n = 0
  for d in number:
    n=n*len(s1)+s1.find(d)
  r = ""
  while n:
    r = s2[n%len(s2)] + r
    n/=len(s2)
  return r

def bacon(c,k):
  l=len(c)
  ret=""
  for i in range(0,l):
    n=str(a.find(c[i]))
    a1=switch_base(n,dec,"01")
    r=""
    for j in range(0,5):
      if 5-j>len(a1):
        r=r+a[a.find(k[(i*5+j)%len(k)])]
      elif a1[len(a1)+j-5]=="1":
        r=r+b[a.find(k[(i*5+j)%len(k)])]
      else:
        r=r+a[a.find(k[(i*5+j)%len(k)])]
    ret=ret+r
  return ret

def c_bacon(c):
  if len(c)%5 != 0:
    return 0
  n=""
  r=""
  for i in range(0,len(c)):
    if a.find(c[i]) == -1:
      n=n+"1"
    else:
      n=n+"0"
    if i%5 == 4:
      r=r+b[int(n,2)]
      n=""
  return r

def base64(c):
  import base64
  return base64.b64encode(c)

def c_base64(c):
  import base64
  return base64.b64decode(c)

def alp2num(c,p):
  result=""
  for i in c:
    result=result+p+str(a.find(i)+1)
  return result

def a2n(c):
 result=""
 for i in c:
  s=str(a.find(i)+1)
  if a.find(i)<=8:
   s="0"+str(a.find(i)+1)
  result=result+s
 return result

def num2alp(c,p):
  num=""
  result=""
  for i in c:
    if i==p:
      result=result+b[int(num)-1]
      num=""
    else:
      num=num+i
  return result

def n2a(c):
 result=""
 if len(c)%2==1:
  return 0
 r=""
 for i in range(0,len(c)):
  r=r+c[i]
  if i%2==1:
   result=result+a[int(r)-1]
   r=""
 return result

def reverse(c):
  result=""
  for i in c:
    result=i+result
  return result

def rot13(c):
  return caeser(c,13)

def caeser(c,y):
  result = ""
  for i in c:
    result=result+b[(a.find(i)+y)%26]
  return result

def a_caeser(c):
  for j in range(1,26):
    print "key:",j,"output:",caeser(c,j)

def c_caeser(c,y):
  return caeser(c,(26-y)%26)

def ca_caeser(c):
  for j in range(26,0,-1):
    print "key:",j,"output:",caeser(c,j)

def ccaeser(a,b,c,d):
  if a=="c":
    b=(26-b)%len(d)
  l = len(c)
  result = ""
  for i in range(0,l):
    result=result+d[(d.find(c[i])+b)%len(d)]
  print result
'''
def vigenere(c,y):
  result=""
  l=len(c)
  m=len(y)
  for i in range(0,l):
    j=i%m
    for k in range(0,26):
      if y[j]==a[k] or y[j]==b[k]:
        break
    result = result + caeser(c[i],k)
  return result
'''
def vigenere(c,y):
  result=""
  l=len(c)
  m=len(y)
  for i in range(0,l):
    j=i%m
    result = result + b[(a.find(c[i])+a.find(y[j]))%26]
  return result
'''
def c_vigenere(c,y):
  l=len(y)
  j=""
  for i in range(0,l):
    for k in range(0,26):
      if y[i]==a[k]:
        break
    j=j+a[(26-k)%26]
  return vigenere(c,j)
'''
def c_vigenere(c,y):
  result=""
  l=len(c)
  m=len(y)
  for i in range(0,l):
    j=i%m
    result = result + b[(a.find(c[i])-a.find(y[j]))%26]
  return result

def a_vigenere(c,y):
  for i in y:
    print "key:",i,"result:",vigenere(c,i)

def asci(c):
  result=""
  l=len(c)
  for i in range(0,l):
    result=result+" "+str(int(ord(c[i])))
  return result

def c_asci(c):
  num=""
  result=""
  l=len(c)
  for i in range(0,l):
    if c[i]==" ":
      result=result+chr(int(num))
      num=""
    else:
      num=num+c[i]
  return result

if mode == 1:
#caeser cipher
  print caeser(cipher, key)
if mode == 2:
#Vigenere cipher
  print vigenere(cipher, key)
if mode == 3:
#ASCII
  print asci(cipher)
if mode == 4:
#alphabet to number
  print alp2num(cipher," ")
  print a2n(cipher,"")
if mode == 5:
  print base64(cipher)
if mode == 6:
#bacon
  print bacon(cipher,key)
#
if mode == 11:
#counter caeser
  print c_caeser(cipher, key)
if mode == 12:
#counter vigenere
  print c_vigenere(cipher, key)
if mode == 13:
#counter ASCII
  print c_asci(cipher)
if mode == 14:
#number to alphabet
  print num2alp(cipher," ")
  print n2a(cipher)
if mode == 15:
  print c_base64(cipher)
if mode == 16:
#counter bacon
  print c_bacon(cipher)
#
if mode == 20:
  print reverse(cipher)
if mode == 21:
  print rot13(cipher)
if mode == 22:
  a_caeser(cipher)
if mode == 23:
  a_vigenere(cipher, key)
if mode == 24:
  ccaeser(m,key,cipher,i)
if mode == 25:
  print switch_base(cipher,dec,"01")