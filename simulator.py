inp_file_path=input("please enter the input file path or just drag and drop here. = ")
output_test_file_path = input("please enter the output test file path or just drag and drop here = ")

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
        
print(count) 