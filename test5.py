#删除训练集中不是li类的某个类的所有样本
try:
    file = open('MR_3_tran5.txt',"r")
    file1 = open('MR_4_tran5.txt',"w")
except FileNotFoundError:
    print("file is not found")
else:
    contents = file.readlines()
    for content in contents:
        if content.count('\n')==len(content):#判断此行是否为空行
            print("111")
        else:
            #print(content.split('\t')[0] + "\thhhh\t" + content.split('\t')[1])
            file1.write(
                content.split('\t')[0] + "\t" + content.split('\t')[1] + "\t" + content.split('\t')[2] + "\t" +
                content.split('\t')[3] + "\t" + content.split('\t')[4] + "\t" + content.split('\t')[5] + "\t" +
                content.split('\t')[6] + "\t" + content.split('\t')[7] + "\t" + content.split('\t')[8] + "\t" +
                content.split('\t')[8] + "\t" + content.split('\t')[9] + "\t" + content.split('\t')[10] + "\t" +
                content.split('\t')[11] + "\t" + content.split('\t')[12] + "\n")