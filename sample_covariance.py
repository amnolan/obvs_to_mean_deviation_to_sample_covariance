#work in progress
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
# def pretty_print(ra):
#     for x, item in enumerate(ra):
#         if x == len(ra)-1:
#             str(item)
#         else:
#             str(item)+ " "

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
#print(parent_ra)
n = len(parent_ra[0])
print(n)

copy_parent_ra = two_d_deep_copy(parent_ra)
print(parent_ra)
print(copy_parent_ra)

# iterate over each vector
# for count in range(0,n):
#     parent_ra[0][count] = (1/n)*parent_ra[0][count]
#     parent_ra[1][count] = (1/n)*parent_ra[1][count]

# print(parent_ra)
# print(copy_parent_ra)
