#交换训练集中任意两列
try:
    file = open('Contact lenses.txt',"r")
    file1 = open('MR_1_all0.txt',"w")
except FileNotFoundError:
    print("file is not found")
else:
    contents = file.readlines()
    matrix = [1,0,3,2,4]
    for content in contents:
        if content.count('\n')==len(content):#判断此行是否为空行
            print("111")
            #105264397(10)8
        else:
            #print(content.split('\t')[0] + "\thhhh\t" + content.split('\t')[1])
            file1.write(content.split('\t')[matrix[0]] + "\t" + content.split('\t')[matrix[1]] + "\t" + content.split('\t')[matrix[2]] +"\t"+ content.split('\t')[matrix[3]] +"\t"+ content.split('\t')[matrix[4]] + "\n")