# Chương trình nhập vào 2 số X, Y từ đó xây dựng mảng 2 chiều. Giá trị của mỗi phần tử tại hàng i, cột j sẽ bằng i*j.
input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)