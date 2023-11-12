def convert_to_float(input_row):
    output_row = []
    for i in input_row:
        output_row.append(float(i))
    return output_row

def two_d_deep_copy(src_array):
    dest_array = []
    for i in range(0,len(src_array)):
        sub_ra = []
        for j in range(0,len(src_array[i])):
            sub_ra.append(src_array[i][j])
        dest_array.append(sub_ra)
    return dest_array

def total_up_mean_matrix(ra):
    totals_list = []
    for i in range(0,len(ra)):
        total = 0
        for j in range(0,len(ra[i])):
            total += ra[i][j]
        totals_list.append(total)
    return totals_list

def get_x_hat_array(ra,mean_vector):
    #iterate over vectors
    for i in range(0,len(ra[0])):
        ra[0][i] = (ra[0][i] - mean_vector[0])
        ra[1][i] = (ra[1][i] - mean_vector[1])
    return ra

def transpose_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed_matrix = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

def matrix_multiply(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    # Check if the matrices can be multiplied
    if cols1 != rows2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the result matrix with zeros
    result_matrix = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

def multiply_matrix_by_scalar(matrix, scalar):
    # Iterate through the matrix and multiply each element by the scalar
    result_matrix = [[element * scalar for element in row] for row in matrix]
    return result_matrix

def sample_mean(matrix, n):
    top = []
    bottom = []
    container = []
    for count in range(0,n):
        top.append((1/n)*parent_ra[0][count])
        bottom.append((1/n)*parent_ra[1][count])
    container.append(top)
    container.append(bottom)
    return container

print("Convers Mtrx of obsvsn to mean-deviation form")
print("Given matrix A create M=(1/N)[X_1,X_2...X_N]")
print("Input top row of matrix comma separated")
top_row = convert_to_float((input()).split(","))
print("Input bottom row of matrix comma separated")

bottom_row = convert_to_float((input()).split(","))
# top_row = [14,6,9,16,6,19]
# bottom_row = [3,15,8,7,6,5]
parent_ra = []
parent_ra.append(top_row)
parent_ra.append(bottom_row)

n = len(parent_ra[0])
print("Size (n):",n)

#save the original state
original_ra = two_d_deep_copy(parent_ra)

sample_mean_ra = sample_mean(two_d_deep_copy(parent_ra), n)
print("Sample Mean Matrix: ")
print(sample_mean_ra)
print("Sample Mean Matrix totalled: [top, bottom] respectively")
sample_mean_mtrx = total_up_mean_matrix(sample_mean_ra)
print(sample_mean_mtrx)
print("Press any key to proceed:")
input()
print("Finding Xhat for each vector")

x_hat_ra = two_d_deep_copy(parent_ra)
x_hat_ra = get_x_hat_array(x_hat_ra,sample_mean_mtrx)
print("B (matrix of Xhat vectors)\n")
print(x_hat_ra)
print("Press any key to proceed")
input()
print("Sample covariance matrix is S=(1/N-1)*B*B^Transpose")
b_transpose = transpose_matrix(x_hat_ra)
print("B^Transpose")
print(b_transpose)
print("Press any key to proceed")
input()
print("B*B^Transpose is:")
sample_cov_mtrx = matrix_multiply(x_hat_ra,b_transpose)
print(sample_cov_mtrx)
print("Press any key to proceed")
input()
final_sample_cov_matrix = multiply_matrix_by_scalar(sample_cov_mtrx,1/(n-1))
print(final_sample_cov_matrix)
