from multiprocessing import Process, Pool

def element(index, A, B, res):
    glodal res
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res

res = 0

p1 = Process(target=element, args=[(0, 0), matrix1, matrix2, res])
p1.start()
p1.join()

print(res)
