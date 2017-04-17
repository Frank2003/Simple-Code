def goto(i,start,s):
    right=0
    left=0
    if start=="]":
        right+=1
    if start=="[":
        left+=1
    while i>=0 and i<len(s) and left!=right:
        if start=="]":
            i-=1
        if start=="[":
            i+=1
        if s[i]=="]":
            right+=1
        if s[i]=="[":
            left+=1
    return i

def interpret(s,out_,delay,one):
    width=256
    cellmax=256
    cells=[0]*cellmax
    i=0 #Current executing Location
    if "," in s:
        inp=raw_input("Input:")
    outp=""
    read=0
    pointer=0
    while i<len(s):
        if s[i]=="+":
            cells[pointer]=(cells[pointer]+1)%width
        if s[i]=="-":
            cells[pointer]=(cells[pointer]-1)%width
        if s[i]==">":
            pointer=(pointer+1)%cellmax
        if s[i]=="<":
            pointer=(pointer-1)%cellmax
        if s[i]=="]":
            i=goto(i,"]",s)
        if s[i]=="[" and cells[pointer]==0:
            i=goto(i,"[",s)
        if s[i]=="," and read<len(inp):
            cells[pointer]=ord(inp[read])
            read+=1
        elif s[i]==",":
            cells[pointer]=0
        if out_:
            print s,"\n"," "*i+"^",s[i]
        flag=0
        if out_:
            out=""
            for j in range(pointer-3,pointer+4):
                out=out+"[%d]"%(cells[j%cellmax])
                if j==pointer:
                    flag=len(out)-2
            print out,"\n"+" "*flag+"^",pointer
            sleep(delay)
        if s[i]==".":
            print "Output:",cells[pointer],chr(cells[pointer])
            outp=outp+chr(cells[pointer])
        if one and out_:
            raw_input()
        i+=1
    print "Total:",outp
