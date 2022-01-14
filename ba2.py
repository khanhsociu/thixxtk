name = str(input("Nhập tên đệm"))
print("tên của bạn: ",name);
def demkytutrongtenvatendem():
    count_lower1 = 0
    for c in s:
        if c.islower():
            count_lower1 += 1

    count_lower2 = 0
    for c in n:
        if c.islower():
            count_lower2 += 1
    print("Xuất tên sinh viên:", s .title() + n .title())
    print("Số ký tự trong tên đệm:", count_lower1)
    print("Số ký tự trong tên:", count_lower2)

s = str(input("Nhập tên đệm sinh viên: "))
n = str(input("Nhập tên của sinh viên: "))
demkytutrongtenvatendem()

def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;


n = int(input("Nhập số nguyên dương n = "));
print("các chữ số của", n, "là", totalDigitsOfNumber(n));