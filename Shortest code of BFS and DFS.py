import copy
M = [[3, 2, 1],[ 4,5,6],[8,7,0]]
# M = [[ 1, 2, 3],[ 4, 5, 6],[7, 8, 0]] 
destination_matrix = [[ 1, 2, 3],[ 4, 5, 6],[7, 8, 0]] 

def matrix(m,n):
    M = [ ]
    for i in range(m):
        row = [ ]
        for j in range(n):
            element = int(input(f' enter element M {i} {j} '))
            row.append(element)
        M.append(row)
    return M

all_matrix = [ ]
all_matrix.append(M)
print(all_matrix)
def upword_move(randomA):
    for i in range(3):
        for j in range(3):
            if randomA[i][j] == 0:
                if i!=0:
                    randomA[i][j]= randomA[i-1][j]
                    randomA[i - 1][j]=0
                    return randomA
                    
def downward_move(randomB):
    for i in range(3):
        for j in range(3):
            if randomB[i][j] == 0:
                if i!=2:
                    randomB[i][j]= randomB[i+1][j]
                    randomB[i + 1][j]=0
                    return randomB
                    
def left_move(randomD):
    for i in range(3):
        for j in range(3):
            if randomD[i][j] == 0:
                if j!=0:
                    randomD[i][j]= randomD[i][j-1]
                    randomD[i ][j-1]=0
                    return randomD
                    
def right_move(randomC):
    for i in range(3):
        for j in range(3):
            if randomC[i][j] == 0:
                if j!=2:
                    randomC[i][j]= randomC[i][j+1]
                    randomC[i][j+1]=0
                    return randomC
b = set()

a = 1
while M!=destination_matrix:
    if(M==destination_matrix):
        break
    A2 = upword_move(copy.deepcopy(M))
    if(A2!=None):
        if str(A2) not in b:
        # if A2 not in all_matrix:
            all_matrix.append(A2)
            b.add(str(A2))
    B1 = copy.deepcopy(M)
    B2 = downward_move(B1)
    if(B2!=None):
        if str(B2) not in b:
        # if B2 not in all_matrix:
            all_matrix.append(B2)
            b.add(str(B2))
    C1 = copy.deepcopy(M)
    C2 = right_move(C1)
    if(C2!=None):
        if str(C2) not in b:
        # if C2 not in all_matrix:
            all_matrix.append(C2)
            b.add(str(C2))
    D1 = copy.deepcopy(M)
    D2 = left_move(D1)
    if(D2!=None):
        if str(D2) not in b:
        # if D2 not in all_matrix:
            all_matrix.append(D2)
            b.add(str(D2))
    
    b.add(str(M))
    # Python code to convert string to list


    M = all_matrix.pop(-1)
    a = a+1
print(a)
print("we got our goal",destination_matrix)






    




