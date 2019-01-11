fileN=open("proopiomelanocortin_CpG.txt","w")
NumberofC=0
NumberofG=0
NumberofCG=0
s=""
V=0
flag=False
##read the fasta file, file name can be changed  
data=open("proopiomelanocortin.fa","r")
seq=""
for x in data:
    if x.startswith(">"):
        continue
    else:
        seq+=x
seq=seq.replace("\n","") 
##calculation for CpG site
for i in range(0,len(seq)-100,1):
    s=seq[i:i+100]
    for a in range(0,100):
        if (s.find('CG')!=-1):
            flag=True
            if (s[a]=="C"):
                NumberofC+=1
                if(a!=99):
                    if (s[a+1]=="G"):
                        NumberofCG+=1
            if(s[a]=="G"):
                NumberofG+=1
        else :
            fileN.write(str(i)+"		"+str(V)+"\n")    
            flag=False
            break
    if(flag==True):
        Exp=(NumberofCG/(NumberofC*NumberofG))*100  
        NumberofC=0
        NumberofG=0
        NumberofCG=0       
        fileN.write(str(i)+"		"+str(Exp)+"\n")
