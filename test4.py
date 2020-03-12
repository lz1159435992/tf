#置换类标签（结果），即互换任意两个类标签
try:
    file = open('Contact lenses.txt',"r")
    file1 = open('MR_3_all2.txt',"w")
except FileNotFoundError:
    print("file is not found")
else:
    contents = file.readlines()
    for content in contents:
        if content.count('\n')==len(content):#判断此行是否为空行
            print("111")
        else:
            if content.split('\t')[4] == 'no lenses\n' or content.split('\t')[4] == 'no lenses' :
                print("222")
                file1.write(
                    content.split('\t')[0] + "\t" + content.split('\t')[1] + "\t" + content.split('\t')[2] + "\t" +
                    content.split('\t')[3] + "\t" + "hard" + "\n\n")
            elif content.split('\t')[4] == 'hard\n':
                file1.write(
                    content.split('\t')[0] + "\t" + content.split('\t')[1] + "\t" + content.split('\t')[2] + "\t" +
                    content.split('\t')[3] + "\t" + "no lenses" + "\n\n")
            else:
                #print(content.split('\t')[6])
                file1.write(
                    content.split('\t')[0] + "\t" + content.split('\t')[1] + "\t" + content.split('\t')[2] + "\t" +
                    content.split('\t')[3] + "\t" + "soft" + "\n\n")