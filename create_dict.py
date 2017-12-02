# -*- coding: cp936 -*-
import requests
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'
}
cnt = 0
indents = 5
a=''
F=open("test.txt","w",encoding="utf-8")

def run(qury):
    global total
    url="http://dict.cn/"+qury
    req = requests.get(url, headers=headers, timeout=20).content
    #time.sleep(0.5)
    try:
        F.write(str(cnt)+"."+qury)
        s=req.decode("utf-8")
        start=s.find('<ul class="dict-basic-ul">')
        end=s.find('<li style="padding-top: 25px;">')
        S=s[start:end]
        cur=0
        indent = indents-len(str(cnt)+"."+qury)//4
        first=True
        while(1):
            a=S[cur:].find('<span>')+cur
            b=S[cur:].find('</span>')+cur
            c=S[cur:].find('<strong>')+cur
            d=S[cur:].find('</strong>')+cur
            if d==cur-1: break
            if first:
                F.write('\t'*indent)
            else:
                F.write('\t'*indents)
            if a!=cur-1: F.write(S[a+6:b])
            F.write(S[c+8:d]+'\n')
            cur=d+1
            first=False
        if first:
            F.write("\n")
        F.flush()
    finally:
        pass

I=open("words_alpha.txt","r")
l=""
done=False
try:
    while(1):
        cnt+=1
        l=I.readline()
        if not l: break
        done=False
        run(l.strip('\n '))
        done=True
        print(cnt)
except Exception as e:
    if done: l=I.readline()
    print(l,e,"\n")
    I.close()
F.close()
