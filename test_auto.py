in_files=["a_an_example.in.txt","b_basic.in.txt","c_coarse.in.txt","d_difficult.in.txt","e_elaborate.in.txt"]
out_files=["a_an_example","b_basic","c_coarse","d_difficult","e_elaborate"]

threshold_val=int(input("enter threshold value = "))
for k in range(5):
    
    in_file_str=r"D:\vscode_projects\python\hashcode_2022\practice\input"+"\\"+in_files[k]
    out_file_str=r"D:\vscode_projects\python\hashcode_2022\practice\output_test_hanshika"+"\\"+out_files[k]+".txt"
    
    in_file = open(in_file_str,'r')
    out_file = open(out_file_str,'w')

    total_input=in_file.readline()
    T=int(total_input)
    data_dict={}
    max_dislike=0
    for __ in range(T):
        likes=(in_file.readline().split())[1:]
        dislikes=(in_file.readline().split())[1:]
        
        for i in likes:
            if i in data_dict.keys():
                (data_dict[i])[0]+=1
            else:
                data_dict[i]=[1,0]
                
        for i in dislikes:
            if i in data_dict.keys():
                data_dict[i][1]+=1
                if data_dict[i][1]>max_dislike:
                    max_dislike=data_dict[i][1]
            else:
                data_dict[i]=[0,1]


    threshold=max_dislike*(threshold_val/100)
    length=0
    output=' '
    for i in data_dict:
        if data_dict[i][0]>data_dict[i][1] or data_dict[i][1]<threshold:
            length+=1
            output+=i+' '
    out_file.write(str(length)+output)