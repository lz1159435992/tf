# -*- coding:utf-8 -*-
import operator
import numpy as np
import os
import time
import random
import math
import re
start = time.clock()
N = 100
D = 2
K = 3
def gedata():
    X = np.zeros((N * K, D))
    y = np.zeros(N * K, dtype='uint8')
    Xy = np.zeros((N * K, D+1))
    for j in range(K):
        ix = range(N * j, N * (j + 1))
        r = np.linspace(0.0, 1, N)
        t = np.linspace(j * 4, (j + 1) * 4, N) + np.random.randn(N) * 0.2
        X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
        y[ix] = j
    #拼接两个矩阵
    Xy = np.c_[X, y]
    np.savetxt("Xy.txt",Xy)
    np.savetxt("X.txt",X)
    np.savetxt("y.txt",y)
    return Xy

def loaddata(filepath):
    A = np.zeros((N * K, D+1))  # 先创建一个 3x3的全零方阵A，
    f = open(filepath)  # 打开数据文件文件
    print(filepath.split("\\"))
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    A_row = 0  # 表示矩阵的行，从0行开始
    for line in lines:  # 把lines中的数据逐行读取出来
        list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        #?
        A[A_row:] = list[0:3]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        A_row += 1  # 然后方阵A的下一行接着读
        # print(line)
    print(A)  # 打印 方阵A里的数据
    X = A[:,0:2] #B为前两列数据
    y = A[:,2:len(A[0])] #C为最后一列数据
    print(y)
   # print(B)
    #print(C)
 #mr0已弃用
def mr0(filepath,max):
    A = np.zeros((N * K, 3))  # 先创建一个 3x3的全零方阵A，
    B = np.zeros((int(N * K/10*9), D + 1))
    C = np.zeros((int(N * K/10), D + 1))
    f = open(filepath)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    A_row = 0  # 表示矩阵的行，从0行开始
    for line in lines:  # 把lines中的数据逐行读取出来
        list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        A[A_row:] = list[0:3]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        A_row += 1  # 然后方阵A的下一行接着读
    for index in range(10):
        for row in range(300):
            if row % 10 == index:
                C = np.row_stack(C, A[row:])
            else:
                B = np.row_stack(C, A[row:])
        # B = A[0:int(index*max/10), :]
        # C = A[int(index*max/10):int((index+1)*max/10), :]
        # D = A[int((index+1)*max/10):max, :]
        # E = np.vstack((B, D))
        print(C)
        print(B)
        if not os.path.exists('C:\\biyesheji\\data\\' + str(index + 1) + 'fold\\mr0\\'):#若不存在路径则创建
            os.makedirs('C:\\biyesheji\\data\\' + str(index + 1) + 'fold\\mr0\\')
        np.savetxt('C:/biyesheji/data/' + str(index + 1) + 'fold/mr0/train.txt', B)
        np.savetxt('C:/biyesheji/data/' + str(index + 1) + 'fold/mr0/test.txt', C)
def mr1(filepath, targetpath):
    # 交换任意两行
    count = len(open(filepath, 'rU').readlines())
    print(count)
    file = open(filepath, 'r')
    j = 1
    hang = count
    money = []
    for j in range(hang):
        row_content = file.readline()
        money.append(row_content)

    # for index in range(0,len(money)):
    #      print(str(index+1)+" "+money[index])

   # for (i, j) in [(x, x) for x in range(1, hang+1, random.randint(1, int(hang/5)))]:
    for (i, j) in [(x, x) for x in random.sample(range(1, hang+1), 4)]:
       # for (i1, j1) in [(x1, x1) for x1 in range(i + 1, hang+1, random.randint(1, int(hang/5)))]:
        for (i1, j1) in [(x1, x1) for x1 in random.sample(range(1, hang+1), 4)]:
            name = targetpath+"tran_row_" + str(i) + "_" + str(i1)
            # print(name)

            for index in range(0, len(money)):
                if (index + 1) == i:
                    one = money[index]
                    # print(str(i)+one)
                if (index + 1) == i1:
                    two = money[index]
                    # print(str(i1)+two)

            for index in range(0, len(money)):
                if (index + 1) == i:
                    money[index] = two
                if (index + 1) == i1:
                    money[index] = one

            for index in range(0, len(money)):
                # print(str(index + 1) + " " + money[index])
                with open(name + '.txt', 'a') as fp:
                    fp.write(money[index])

            for index in range(0, len(money)):
                if (index + 1) == i:
                    money[index] = one
                if (index + 1) == i1:
                    money[index] = two
def mr2(filepath, targetpath):
    # 交换训练集中任意两列
    try:
        file = open(filepath, "r")
        file1 = open(targetpath+'tran_column_1_2.txt', "w")
    except FileNotFoundError:
        print("file is not found")
    else:

        contents = file.readlines()
        #matrix = [1, 0, 2]
        for content in contents:
            #print(contents)
            if content.count('\n') == len(content):  # 判断此行是否为空行
                print("111")
                # 105264397(10)8
            else:
                list = content.strip('\n').split(' ')
                #print(list[2])
                #print(content.split('\t'))
                #print(content.split('\t')[0] + "\thhhh\t" + content.split('\t')[1])
                file1.write(list[1] + "\t" + list[0] + "\t" +list[2] + "\n")

def mr3(filepath, targetpath, M, A):#前两个数据变为原来的K倍
    #A = np.zeros((N * K, 3))
    f = open(filepath)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    # 表示矩阵的行，从0行开始
    for k in M:
        A_row = 0
        for line in lines:  # 把lines中的数据逐行读取出来
            list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
            A[A_row:] = list[0:3]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
            A_row += 1
        print(A)
        for i in range(len(A)):
            for j in range(len(A[0])-1):
                A[i][j] = A[i][j] * k
        np.savetxt(targetpath+"X"+str(k)+".txt", A)
#mr0('C:/biyesheji/data/Xy.txt',300)
def mr4(filepath, targetpath, A):#关于y=-x对称
    f = open(filepath)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    # 表示矩阵的行，从0行开始
    A_row = 0
    for line in lines:  # 把lines中的数据逐行读取出来
        list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        A[A_row:] = list[0:3]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        A_row += 1
    print(A)
    for i in range(len(A)):
        B = A[i]
        for j in range(len(A[0]) - 1):
            if j == 0:
                A[i][j] = -B[j+1]
            elif j == 1:
                A[i][j] = -B[j-1]
    np.savetxt(targetpath + "y=-x_change.txt", A)
def mr5(filepath, targetpath, M, A):##前两个数据加k
    f = open(filepath)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    # 表示矩阵的行，从0行开始
    for k in M:
        A_row = 0
        for line in lines:  # 把lines中的数据逐行读取出来
            list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
            A[A_row:] = list[0:3]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
            A_row += 1
        print(A)
        for i in range(len(A)):
            for j in range(len(A[0]) - 1):
                A[i][j] = A[i][j] + k
        np.savetxt(targetpath + "move_" + str(k) + ".txt", A)
def mr6(filepath, targetpath, M, A):#坐标系旋转，不能扩展到其他方法中
    f = open(filepath)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    # 表示矩阵的行，从0行开始
    for k in M:#弧度
        A_row = 0
        for line in lines:  # 把lines中的数据逐行读取出来
            list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
            A[A_row:] = list[0:3]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
            A_row += 1
        print(A)
        for i in range(len(A)):
            x = A[i][0]
            y = A[i][1]
            A[i][0] = x * math.cos(k) + y * math.sin(k)
            A[i][1] = -(x * math.sin(k)) + y * math.cos(k)
        np.savetxt(targetpath + "spin_" + str(k) + ".txt", A)
def allmr1_(filepath_):
    for i in range(10):
        for dirpath, dirnames, filenames in os.walk(filepath_+'\\'+str(i+1)+'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    print(1)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr1\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr1\\')
                    mr1(os.path.join(dirpath, filepath), filepath_+'\\'+str(i+1)+'fold\\mr1\\train_')
                    print(2)
def allmr1():
    for i in range(10):
        for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\'+str(i+1)+'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    print(1)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr1\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr1\\')
                    mr1(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\'+str(i+1)+'fold\\mr1\\train_')
def allmr2_(filepath_):
    for i in range(10):
        if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk(filepath_+'\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    print(1)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr2\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr2\\')
                    mr2(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr2\\train_')
                elif filepath == "test.txt":
                    print(2)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr2\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr2\\')
                    mr2(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr2\\test_')
def allmr2():
    for i in range(10):
        if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    print(1)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr2\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr2\\')
                    mr2(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr2\\train_')
                elif filepath == "test.txt":
                    print(2)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr2\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr2\\')
                    mr2(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr2\\test_')
def allmr3_(filepath_):
    M = random.sample(range(1, 10), 5)
    for i in range(10):
        if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk(filepath_+'\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr3\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr3\\')
                    mr3(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr3\\train_', M, A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr3\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr3\\')
                    mr3(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr3\\test_', M, A)

def allmr3():
    M = random.sample(range(1, 10), 5)
    for i in range(10):
        if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr3\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr3\\')
                    mr3(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr3\\train_', M, A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr3\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr3\\')
                    mr3(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr3\\test_', M, A)
def allmr4_(filepath_):
    for i in range(10):
        if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk(filepath_+'\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr4\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr4\\')
                    mr4(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr4\\train_', A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr4\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr4\\')
                    mr4(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr4\\test_', A)

def allmr4():
    for i in range(10):
        if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr4\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr4\\')
                    mr4(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr4\\train_', A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr4\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr4\\')
                    mr4(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr4\\test_', A)
def allmr5_(filepath_):
    M = np.random.random(5)
    for i in range(10):
        if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk(filepath_+'\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr5\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr5\\')
                    mr5(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr5\\train_', M, A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr5\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr5\\')
                    mr5(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr5\\test_', M, A)
def allmr5():
    M = np.random.random(5)
    for i in range(10):
        if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr5\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr5\\')
                    mr5(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr5\\train_', M, A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr5\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr5\\')
                    mr5(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr5\\test_', M, A)
def allmr6_(filepath_):
    M = np.random.uniform(0, 3.14, 5)
    for i in range(10):
        if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk(filepath_+'\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr6\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr6\\')
                    mr6(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr6\\train_', M, A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists(filepath_+'\\' + str(i + 1) + 'fold\\mr6\\'):
                        os.makedirs(filepath_+'\\' + str(i + 1) + 'fold\\mr6\\')
                    mr6(os.path.join(dirpath, filepath), filepath_+'\\' + str(i + 1) + 'fold\\mr6\\test_', M, A)

def allmr6():
    M = np.random.uniform(0, 3.14, 5)
    for i in range(10):
        if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\'):
            os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\')
        for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
            for filepath in filenames:
                print(os.path.join(dirpath, filepath))
                print(filepath)
                if filepath == "train.txt":
                    A = np.zeros((int(N * K/10*9), 3))
                    print(1)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr6\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr6\\')
                    mr6(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr6\\train_', M, A)
                elif filepath == "test.txt":
                    A = np.zeros((int(N * K / 10), 3))
                    print(2)
                    if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr6\\'):
                        os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr6\\')
                    mr6(os.path.join(dirpath, filepath), 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr6\\test_', M, A)

#filepath2 变异程序 filepath1 蜕变训练集路径
def checkout(y1, y2, filepath1, filepath2):
 #   read_dictionary = {}
    filepath_ = ''
    flag = 0
    lines1 = filepath2.split("\\")
    path1 = lines1[len(lines1)-1]#程序名字
    lines2 = filepath1.split("\\")
    path2 = lines2[len(lines2)-1]#测试集名字
    tuibianclass = lines2[len(lines2)-2]#蜕变测试类别名字
    folds = lines2[len(lines2)-3]
    for i in range(len(y1)):
        if int(y1[i]) != int(y2[i]):
            flag = flag + 1
            print(i)
    for i in range(len(lines2)-3):
        if i == 0:
            filepath_ = lines2[i]
        else:
            filepath_ = filepath_ + '\\' + lines2[i]
    print(filepath_)
    if not os.path.exists(filepath_+'\\' + tuibianclass + '\\'):
        os.makedirs(filepath_+'\\' + tuibianclass + '\\')
    if not os.path.exists(filepath_+'\\' + tuibianclass + '\\result.npy'):
        read_dictionary = {}
        np.save(filepath_+'\\' + tuibianclass + '\\result.npy', read_dictionary)
    read_dictionary = np.load(filepath_+'\\' + tuibianclass + '\\result.npy', allow_pickle = True).item()
    read_dictionary[folds+"+"+path2+"+"+path1] = flag
    np.save(filepath_+'\\' + tuibianclass + '\\result.npy', read_dictionary)
    #最终结果处理

def clearmr(x):
    read_dictionary = {}
    np.save('C:\\biyesheji\\data\\mr'+str(x)+'\\result.npy', read_dictionary)
    re_dict = {}
    np.save('C:\\biyesheji\\data\\mr' + str(x) + '\\mr_result.npy', re_dict)
def readmr_(x, filepath_):
    read_dictionary = {}
    re_dict = {}
    if not os.path.exists(filepath_ + '\\mr' + str(x)):
        os.makedirs(filepath_ + '\\mr' + str(x))
    elif not os.path.exists(filepath_ + '\\mr' + str(x) + '\\result.npy'):
        np.save(filepath_ + '\\mr' + str(x) + '\\result.npy', read_dictionary)
    list = []
    read_dictionary = np.load(filepath_ + '\\mr'+str(x)+'\\result.npy', allow_pickle = True).item()
    if read_dictionary:
        #print(read_dictionary)
        for (key, value) in read_dictionary.items():
            print(key + '  :  ' + str(value))
            lines = key.split('+')
            list.append(lines[2])
        list = set(list)
        if not os.path.exists(filepath_ + '\\mr'+str(x)+'\\mr_result.npy'):
            np.save(filepath_ + '\\mr'+str(x)+'\\mr_result.npy', re_dict)
        for i in list:
            re_dict[i] = 0
        for (key, value) in read_dictionary.items():
            lines = key.split('+')
            if value > 0 :
                re_dict[lines[2]] = re_dict[lines[2]] + 1
        np.save(filepath_ + '\\mr' + str(x) + '\\mr_result.npy', re_dict)
    return re_dict
def readmr(x):
    list = []
    read_dictionary = np.load('C:\\biyesheji\\data\\mr'+str(x)+'\\result.npy', allow_pickle = True).item()
    #print(read_dictionary)
    for (key, value) in read_dictionary.items():
        print(key + '  :  ' + str(value))
        lines = key.split('+')
        list.append(lines[2])
    list = set(list)
    re_dict = {}
    if not os.path.exists('C:\\biyesheji\\data\\mr'+str(x)+'\\mr_result.npy'):
        np.save('C:\\biyesheji\\data\\mr'+str(x)+'\\mr_result.npy', re_dict)
    for i in list:
        re_dict[i] = 0
    for (key, value) in read_dictionary.items():
        lines = key.split('+')
        if value > 0 :
            re_dict[lines[2]] = re_dict[lines[2]] + 1
    for (key, value) in re_dict.items():
        print(key + '  :  ' + str(value))
    np.save('C:\\biyesheji\\data\\mr' + str(x) + '\\mr_result.npy', re_dict)
def clearmr2():
    read_dictionary = {}
    np.save('C:\\biyesheji\\data\\mr2\\result.npy', read_dictionary)
def readmr2():
    read_dictionary = np.load('C:\\biyesheji\\data\\mr2\\result.npy', allow_pickle = True).item()
    #print(read_dictionary)
    for (key, value) in read_dictionary.items():
        print(key + '  :  ' + str(value))
def clearmr3():
    read_dictionary = {}
    np.save('C:\\biyesheji\\data\\mr3\\result.npy', read_dictionary)
def readmr3():
    read_dictionary = np.load('C:\\biyesheji\\data\\mr3\\result.npy', allow_pickle = True).item()
    #print(read_dictionary)
    for (key, value) in read_dictionary.items():
        print(key + '  :  ' + str(value))
def del_file(x):
    for i in range(10):
        ls = os.listdir('C:\\biyesheji\\data\\'+str(i+1)+'fold\\mr'+str(x))
        for j in ls:
            c_path = os.path.join('C:\\biyesheji\\data\\'+str(i+1)+'fold\\mr'+str(x), j)
            if os.path.isdir(c_path):
                del_file(c_path)
            else:
                 os.remove(c_path)

#filepath1_测试数据路径#filepath2_测试程序路径
def gettest_(filepath1_,filepath2_):  # 原始测试集测出的结果 (该方法只针对了原始程序) 对变异程序修改后已经可以生成
    for i in range(10):
        for dirpath, dirnames, filenames in os.walk(filepath1_+'\\' + str(i + 1) + 'fold\\mr0'):
            filename2 = filepath1_+'\\' + str(i + 1) + 'fold\\mr0\\test.txt'
            for filepath in filenames:
                if filepath == "train.txt":
                    for dirpath1, dirnames1, filenames1 in os.walk(filepath2_):
                        for filepath1 in filenames1:
                            print(os.path.join(dirpath, filepath))
                            print(filepath)
                            os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath), filename2))


def gettest():#原始测试集测出的结果 (该方法只针对了原始程序) 对变异程序修改后已经可以生成
    for i in range(10):
        for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
            filename2 = 'C:\\biyesheji\\data\\'+str(i+1)+'fold\\mr0\\test.txt'
            for filepath in filenames:
                if filepath == "train.txt":
                    for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code_test'):
                        for filepath1 in filenames1:
                            print(os.path.join(dirpath, filepath))
                            print(filepath)
                            os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath), filename2))
                            #os.system('python C:\\Users\\Zheng\\PycharmProjects\\tf\\classifier_test.py %s %s' % (os.path.join(dirpath, filepath), filename2))
def settestdata():#对每个变异程序产生原始测试集结果 暂时没有写入程序!!!
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
                    filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath == 'train.txt':
                            print(os.path.join(dirpath, filepath))
                            print(os.path.join(dirpath1, filepath1))
                            # if not os.path.exists('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\filepath1'):
                            #     os.makedirs('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\filepath1')
                            # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\filepath1\\test.txt'
                            print(filepath)
                            os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath), filename2))

#filepath1 测试集路径 filepath2 变异分类器程序路径
def gettestdata(filepath1, filepath2):#获取原始测试集所得到的结果的路径,修改完成
    classifiernames = filepath2.split('\\')
    classifiername = classifiernames[len(classifiernames) - 1]
    filetest = ''
    strs = filepath1.split('\\')
    for i in range(len(strs) - 2):
        if i > 0:
            filetest = filetest + "\\" + strs[i]
        elif i == 0:
            filetest = filetest + strs[i]
    #每个分类器一个单独的文件夹
    filetest = filetest + "\\mr0\\"+classifiername+"\\predicted.txt"
    return filetest
def testingmr0():
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
#filepath1_数据filepath2_程序
def testingmr1_(filepath_):
    x = 0
    lines = filepath_.split('/')
    filepath1_ = ''
    for i in range(len(lines)-1):
        if i == 0:
            filepath1_ = lines[i]
        else:
            filepath1_ = filepath1_ + '\\' + lines[i]
    print(filepath_)
    print(filepath1_)
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk(filepath1_ + '\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk(filepath_ + '\\' + str(i + 1) + 'fold\\mr1'):
                    filename2 = filepath_ + '\\'+str(i+1)+'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        x = x + 1
                        print(os.path.join(dirpath, filepath))
                        print(os.path.join(dirpath1, filepath1))
                        print(filepath)
                        a = os.system('python '+os.path.join(dirpath1, filepath1)+' %s %s' % (os.path.join(dirpath, filepath), filename2))
                        print(x)
                        print(a)
                        if a == 0:
                            x = x - 1
    return x
                        #os.system('python C:\\Users\\Zheng\\PycharmProjects\\tf\\classifier.py %s %s' % (os.path.join(dirpath, filepath), filename2))

def testingmr1():
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr1'):
                    filename2 = 'C:\\biyesheji\\data\\'+str(i+1)+'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        print(os.path.join(dirpath, filepath))
                        print(os.path.join(dirpath1, filepath1))
                        print(filepath)
                        os.system('python '+os.path.join(dirpath1, filepath1)+' %s %s' % (os.path.join(dirpath, filepath), filename2))
                        #os.system('python C:\\Users\\Zheng\\PycharmProjects\\tf\\classifier.py %s %s' % (os.path.join(dirpath, filepath), filename2))
def testingmr2_(filepath_):
    x = 0
    lines = filepath_.split('/')
    filepath1_ = ''
    for i in range(len(lines) - 1):
        if i == 0:
            filepath1_ = lines[i]
        else:
            filepath1_ = filepath1_ + '\\' + lines[i]
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk(filepath1_ + '\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk(filepath_+'\\' + str(i + 1) + 'fold\\mr2'):
                    #filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        x = x + 1
                                        print(os.path.join(dirpath, filepath))#测试集
                                        print(os.path.join(dirpath1, filepath1))#待测程序
                                        print(os.path.join(dirpath, filepath2))#训练集
                                        a = os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
                                        if a == 0:
                                            x = x - 1
    return x
def testingmr2():
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr2'):
                    #filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        print(os.path.join(dirpath, filepath))#测试集
                                        print(os.path.join(dirpath1, filepath1))#待测程序
                                        print(os.path.join(dirpath, filepath2))#训练集
                                        os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))

def testingmr3_(filepath_):
    x = 0
    lines = filepath_.split('/')
    filepath1_ = ''
    for i in range(len(lines) - 1):
        if i == 0:
            filepath1_ = lines[i]
        else:
            filepath1_ = filepath1_ + '\\' + lines[i]
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk(filepath1_ + '\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk(filepath_ + '\\' + str(i + 1) + 'fold\\mr3'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        x = x + 1
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        a = os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
                                        if a == 0:
                                            x = x - 1
    return x
def testingmr3():
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr3'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
def testingmr4_(filepath_):
    x = 0
    lines = filepath_.split('/')
    filepath1_ = ''
    for i in range(len(lines) - 1):
        if i == 0:
            filepath1_ = lines[i]
        else:
            filepath1_ = filepath1_ + '\\' + lines[i]
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk(filepath1_ + '\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk(filepath_ + '\\' + str(i + 1) + 'fold\\mr4'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        x = x + 1
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        a = os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
                                        if a == 0:
                                            x = x - 1
    return x
def testingmr4():
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk(filepath1_ + '\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr4'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
def testingmr5_(filepath_):
    x = 0
    lines = filepath_.split('/')
    filepath1_ = ''
    for i in range(len(lines) - 1):
        if i == 0:
            filepath1_ = lines[i]
        else:
            filepath1_ = filepath1_ + '\\' + lines[i]
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk(filepath1_ + '\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk(filepath_ + '\\' + str(i + 1) + 'fold\\mr5'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        x = x + 1
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        a = os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
                                        if a == 0:
                                            x = x - 1
    return x
def testingmr5():
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr5'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
def testingmr6_(filepath_):
    x = 0
    lines = filepath_.split('/')
    filepath1_ = ''
    for i in range(len(lines) - 1):
        if i == 0:
            filepath1_ = lines[i]
        else:
            filepath1_ = filepath1_ + '\\' + lines[i]
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk(filepath1_ +'\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk(filepath_ + '\\' + str(i + 1) + 'fold\\mr6'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        x = x + 1
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        a = os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
                                        if a == 0:
                                            x = x - 1
    return x
def testingmr6():
    for i in range(10):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\biyesheji\\code'):
            for filepath1 in filenames1:
                for dirpath, dirnames, filenames in os.walk('C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr6'):
                    # filename2 = 'C:\\biyesheji\\data\\' + str(i + 1) + 'fold\\mr0\\test.txt'
                    for filepath in filenames:
                        if filepath[0:4] == "test":
                            str2 = filepath[4:]
                            for filepath2 in filenames:
                                if filepath2[0:5] == "train":
                                    str1 = filepath2[5:]
                                    if str1 == str2:
                                        print(os.path.join(dirpath, filepath))  # 测试集
                                        print(os.path.join(dirpath1, filepath1))  # 待测程序
                                        print(os.path.join(dirpath, filepath2))  # 训练集
                                        os.system('python ' + os.path.join(dirpath1, filepath1) + ' %s %s' % (os.path.join(dirpath, filepath2), os.path.join(dirpath, filepath)))
def ge_accuracy(path):
    #if not os.path.exists('C:\\aaaaatest\\biyesheji\\data\\acc.npy'):
    if not os.path.exists('C:\\' +path + '\\biyesheji\\data\\acc.npy'):
        acc_dict = {}
        #np.save('C:\\aaaaatest\\biyesheji\\data\\acc.npy', acc_dict)
        np.save('C:\\' +path + '\\biyesheji\\data\\acc.npy', acc_dict)
    else:
        acc_dict = np.load('C:\\' +path + '\\biyesheji\\data\\acc.npy', allow_pickle = True).item()
        #acc_dict = np.load('C:\\aaaaatest\\biyesheji\\data\\acc.npy').item()
    for i in range(10):
        #for dirpath1, dirnames1, filenames1 in os.walk('C:\\aaaaatest\\biyesheji\\data'):
        for dirpath1, dirnames1, filenames1 in os.walk('C:\\' +path + '\\biyesheji\\data'):
            for filepath1 in dirnames1:
                if filepath1[1:5] == "fold" or filepath1[2:6] == "fold":
                    A = np.loadtxt(os.path.join(dirpath1, filepath1)+'\\mr0\\test.txt')
                    A = A[:, 2:len(A[0])]
                    for dirpath2, dirnames2, filenames2 in os.walk(os.path.join(dirpath1, filepath1)+'\\mr0'):
                        for filepath2 in dirnames2:
                            if len(filepath2)>10:
                                B = np.loadtxt(os.path.join(dirpath2, filepath2)+'\\predicted.txt')
                                x = 0
                                for j in range(30):
                                    list1 = A[j:j+1]
                                    list2 = B[j:j+1]
                                    if list1[0] == list2[0]:
                                        x = x+1
                                acc_dict[filepath2 + '+' + filepath1] = x/30
                                # print(B)
                                # print("***********")
                                # print(np.mean(A == B))
                                # acc_dict[filepath2 + '+' +filepath1] = np.mean(A == B)
    #np.save('C:\\aaaaatest\\biyesheji\\data\\acc.npy', acc_dict)
    np.save('C:\\' +path + '\\biyesheji\\data\\acc.npy', acc_dict)
def read_accuracy(path):
    re_dict = {}
    #acc_dict = np.load('C:\\aaaaatest\\biyesheji\\data\\acc.npy').item()
    acc_dict = np.load('C:\\' +path + '\\biyesheji\\data\\acc.npy', allow_pickle = True).item()
    list = []
    # for (key, value) in acc_dict.items():
    #     print(key + '  :  ' + str(value))
    for (key, value) in acc_dict.items():
        keys = key.split("+")
        list.append(keys[0])
    list = set(list)
    for i in list:
        a = 0
        for (key, value) in acc_dict.items():
            keys = key.split("+")
            if keys[0] == i:
                a = a + value
        re_dict[i] = a/10
    for (key, value) in re_dict.items():
        print(key + '  :  ' + str(value))
#os.system("python C:\Users\Zheng\PycharmProjects\tf\classifier.py")

#filename1 = "C:\\biyesheji\\data\\9fold\\mr0\\train.txt"
#filename2 = "C:\\biyesheji\\data\\9fold\\mr0\\test.txt"
#两个%s放在一块写就会把两个字符串变成一个
#os.system('python C:\\Users\\Zheng\\PycharmProjects\\tf\\classifier.py %s %s' %(filename1, filename2))

# subprocess.Popen(['python', 'C:\\Users\\Zheng\\PycharmProjects\\tf\\classifier.py', filename1, filename2], stdin = subprocess.PIPE, stdout=subprocess.PIPE)
#print(p.poll())
#command = '''start cmd /k "d: & cd C:\\Users\\Zheng\\PycharmProjects\\tf\\ & python C:\\Users\\Zheng\\PycharmProjects\\tf\\classifier.py % filename1 % filename2 && exit"'''

#os.system(command)
#testing()
#readmr1()
#clearmr1()
#allmr1()
#clearmr2()
#gettest()
#del_file(3)
#readmr3()
elapsed = (time.clock() - start)
print("Time used:", elapsed)