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
        ra[0][i] = ra[0][i] - mean_vector[0]
        ra[1][i] = ra[1][i] - mean_vector[1]
    return ra
print("Convers Mtrx of obsvsn to mean-deviation form")
print("Given matrix A create M=(1/N)[X_1,X_2...X_N]")
print("Input top row of matrix comma separated")
top_row = convert_to_float((input()).split(","))
print("Input bottom row of matrix comma separated")
bottom_row = convert_to_float((input()).split(","))
parent_ra = []
copy_parent_ra = []
parent_ra.append(top_row)
parent_ra.append(bottom_row)

n = len(parent_ra[0])
print("Size (n):",n)

original_ra = two_d_deep_copy(parent_ra)
print(parent_ra)
print(original_ra)

# iterate over each vector
for count in range(0,n):
    parent_ra[0][count] = (1/n)*parent_ra[0][count]
    parent_ra[1][count] = (1/n)*parent_ra[1][count]
print("Sample Mean Matrix: [top, bottom] respectively")
sample_mean_mtrx = total_up_mean_matrix(parent_ra)
print(sample_mean_mtrx)
print("Press any key to proceed:")
input()
print("Finding Xhat for each vector")

x_hat_ra = two_d_deep_copy(parent_ra)
x_hat_ra = get_x_hat_array(x_hat_ra,sample_mean_mtrx)
print(x_hat_ra)
