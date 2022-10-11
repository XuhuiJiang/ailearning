import numpy as np
matrix_1=np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
matrix_2=np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [3,2,1],
                   [6,5,4],
                   [9,8,7]])
def compute_distance_two_loop(test_martix,train_martix):
    num_test=test_martix.shape[0]
    print("num_test:"+str(num_test))
    num_train=train_martix.shape[0]
    print("num_train:"+str(num_train))
    dists=np.zeros((num_test,num_train))
    for i in range(num_test):
        for j in range(num_train):
            dists[i][j]=np.sqrt(np.sum(np.square(test_martix[i]-train_martix[j])))

    print(dists)

def compute_distance_one_loop(test_martix,train_matrix):
    dists=np.zeros(test_martix.shape[0],train_matrix.shape[0])
    # 注：这里用到了广播机制，test_matrix[i]维度为(3,)，train_matrix维度为(6, 3)，
    # 计算结果维度为(6, 3)，表示 test_matrix[i] 与 train_matrix 各个样本在各个轴的差值，
    # 最后平方后在axis=1维度进行求和。
    for i in range(test_martix.shape[0]):
        dists[i]=np.sqrt(np.sum(np.square(test_martix[i]-train_matrix[i])),axis=1)
    print(dists)

compute_distance_two_loop(matrix_1,matrix_2)
compute_distance_two_loop(matrix_1,matrix_2)

