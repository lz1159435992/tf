#复制训练集中的某一列变成新的一列
try:
    file = open('Contact lenses.txt',"r")
    file1 = open('MR_2_all4.txt',"w")
except FileNotFoundError:
    print("file is not found")
else:
    contents = file.readlines()
    for content in contents:
        if content.count('\n')==len(content):#判断此行是否为空行
            print("111")
        else:
            #print(content.split('\t')[0] + "\thhhh\t" + content.split('\t')[1])
            file1.write(content.split('\t')[0] + "\t" + content.split('\t')[1] + "\t" + content.split('\t')[2] + "\t" +
                        content.split('\t')[3] + "\t" + content.split('\t')[4] + "\t" + content.split('\t')[4] + "\n")