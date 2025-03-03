# Viết chương trình để tính tổng tất cả các số chẵn trong một List
def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

iput_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, iput_list.split(",")))

tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong danh sách là:", tong_chan)