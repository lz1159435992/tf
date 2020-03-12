#添加无关列
try:
    file = open('Contact lenses.txt',"r")
    file1 = open('MR_0_tran5.txt',"w")
except FileNotFoundError:
    print("file is not found")
else:
    contents = file.readlines()
    for content in contents:
        #print(content.split('\t')[0] + "\thhhh\t" + content.split('\t')[1])
        file1.write(content.split('\t')[0] + "\t" + content.split('\t')[1] + "\t" + content.split('\t')[2] +"\t"+ content.split('\t')[3] +"\t"+ content.split('\t')[4] + "\t" + "123" +"\t" + content.split('\t')[5] +"\t"+ content.split('\t')[6] +"\t"+ content.split('\t')[7] +"\t"+ content.split('\t')[8] + "\t" + content.split('\t')[9] +"\t"+ content.split('\t')[10] + "\n")