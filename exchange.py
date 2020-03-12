#交换任意行
file=open('tran.txt','r')
j=1
hang=21
money = []
for j in range(hang):
    row_content=file.readline()
    money.append(row_content)

# for index in range(0,len(money)):
#      print(str(index+1)+" "+money[index])

for (i, j) in [(x,x) for x in range(1, 22)]:
    for (i1, j1) in [(x1, x1) for x1 in range(i+1, 22)]:
        name="tran_row_"+str(i)+"_"+str(i1)
        #print(name)

        for index in range(0, len(money)):
            if(index+1)==i:
                one=money[index]
                #print(str(i)+one)
            if(index+1)==i1:
                two=money[index]
                #print(str(i1)+two)

        for index in range(0, len(money)):
            if(index+1)==i:
                money[index]=two
            if(index+1)==i1:
                money[index]=one

        for index in range(0, len(money)):
            #print(str(index + 1) + " " + money[index])
            with open(name + '.txt', 'a') as fp:
                fp.write(money[index])

        for index in range(0, len(money)):
            if(index+1)==i:
                money[index]=one
            if(index+1)==i1:
                money[index]=two
