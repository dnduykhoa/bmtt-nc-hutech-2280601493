# Viết chương trình để đảo ngược vị trí của các phần tử trong một List
def dao_nguoc_list(lst):
    return lst[::-1]

iput_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, iput_list.split(",")))

list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược là:", list_dao_nguoc)