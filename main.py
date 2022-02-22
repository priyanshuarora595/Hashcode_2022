outfile=open("e_out.txt",'w')
T=int(input())
data_dict={}
for __ in range(T):
    likes=(input().split())[1:] 
    dislikes=(input().split())[1:]
    
    for i in likes:
        if i in data_dict.keys():
            data_dict[i]+=1
        else:
            data_dict[i]=1
    for i in dislikes:
        if i in data_dict.keys():
            data_dict[i]-=1
            if data_dict[i]==0:
                del data_dict[i]
    
    
    
output=str(len(data_dict.keys()))+" "

for i in data_dict.keys():
    output+=str(i)+' '

outfile.write(output)