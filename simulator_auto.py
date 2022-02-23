in_files=["a_an_example.in.txt","b_basic.in.txt","c_coarse.in.txt","d_difficult.in.txt","e_elaborate.in.txt"]
out_files=["a_an_example","b_basic","c_coarse","d_difficult","e_elaborate"]
for k in range(5):
    in_file_str=r"D:\vscode_projects\python\hashcode_2022\practice\input"+"\\"+in_files[k]
    out_file_str=r"D:\vscode_projects\python\hashcode_2022\practice\output_test_hanshika"+"\\"+out_files[k]+".txt"


    inp_file_path=in_file_str
    output_test_file_path = out_file_str

    out_file = open(output_test_file_path,'r')
    in_file = open(inp_file_path,'r')

    ingredients = out_file.readlines()
    ingredients=(ingredients[0].split())[1:]

    total_input=in_file.readline()
    T=int(total_input)

    count=0

    for i in range(T):
        likes=(in_file.readline().split())[1:]
        dislikes=(in_file.readline().split())[1:]

        flag=1
        for j in likes:
            if j not in ingredients:
                flag =0
                break
        if flag==1:
            for j in dislikes:
                if j in ingredients:
                    flag=0
                    break
        
        if flag==1:
            count+=1
            
    print(out_file_str,count) 