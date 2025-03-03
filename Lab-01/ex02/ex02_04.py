# Xây dựng một chương trình nhằm tìm tất cả các số nằm trong khoảng [2000, 3200] sao cho chia hết cho 7 nhưng không phải bội số của 5. 
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
j = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))