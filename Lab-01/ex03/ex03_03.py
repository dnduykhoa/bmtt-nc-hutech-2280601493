def tao_tuple_tu_list(lst):
    return tuple(lst)

iput_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, iput_list.split(",")))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ list:", my_tuple)