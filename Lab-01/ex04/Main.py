from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*************** MENU ***************")
    print("1. Thêm sinh viên.")
    print("2. Cập nhật thông tin sinh viên bởi ID.")
    print("3. Xóa sinh viên bởi ID")
    print("4. Tìm kiếm sinh viên theo tên.")
    print("5. Sắp xếp sinh viên theo điểm trung bình.")
    print("6. Sắp xếp sinh viên theo tên sinh viên.")
    print("7. Hiển thị danh sách sinh viên.")
    print("0. Thoát.")
    print("************************************")
    
    choice = int(input("Nhập lựa chọn của bạn: "))
    if(choice == 1):
        print("\n1. Thêm sinh viên")
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công")
    
    elif(choice == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updatesinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống.")
            
    elif(choice == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if(qlsv.deleteSinhVien(ID)):
                print("Sinh viên có ID = ", ID, " đã bị xóa.")
            else:
                print("Sinh viên có ID = ", ID, " không tồn tại.")
        else:
            print("\nDanh sách sinh viên trống.")
            
    elif(choice == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống.")
            
    elif(choice == 5):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getlistSinhVien())
        else:
            print("\nDanh sách sinh viên trống.")
            
    elif(choice == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên sinh viên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getlistSinhVien())
        else:
            print("\nDanh sách sinh viên trống.")
            
    elif(choice == 7):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getlistSinhVien()) 
        else:
            print("\nDanh sách sinh viên trống.")
            
    elif(choice == 0):
        print("\nThoát chương trình.")
        break
    else:
        print("\nLựa chọn không hợp lệ.")