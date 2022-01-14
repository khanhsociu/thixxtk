ten = str(input("Nhập tên và msv của bạn"))
print("tên của bạn là: ",ten);
ten = ten.replace(" ",",");
print("chuỗi ký tự đầu vào là : ",ten);

l = ten.split(",")
t = tuple(l)
print(l)
print(t)
