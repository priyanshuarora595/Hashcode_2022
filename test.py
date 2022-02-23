outfile=open("d_test_out.txt",'w')
T=int(input())
data_dict={}
max_dislike=0
for __ in range(T):
    likes=(input().split())[1:] 
    dislikes=(input().split())[1:]
    
    for i in likes:
        if i in data_dict.keys():
            (data_dict[i])[0]+=1
        else:
            data_dict[i]=[1,0]
            
    for i in dislikes:
        if i in data_dict.keys():
            data_dict[i][1]+=1
            if data_dict[i][1]>=max_dislike:
                max_dislike=data_dict[i][1]
        else:
            data_dict[i]=[0,1]


threshold=max_dislike*(0.4)
length=0
output=' '
for i in data_dict:
    if data_dict[i][0]>data_dict[i][1] or data_dict[i][1]<threshold:
        length+=1
        output+=i+' '
outfile.write(str(length)+output)