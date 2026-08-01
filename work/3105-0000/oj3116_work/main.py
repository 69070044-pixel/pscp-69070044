"""นวัตกรรมงบประมาณโรงเรียน"""
school_name = input().upper()
key_pass, gen_pass = [], []


def get_ascii(index, text):
    """This is function to return ascii value"""
    return int(ord(text[index]))

# Step 1
# นําอักขระตัวแรกและตัวสุดท้ายของชื่อโรงเรียนที่เป็นอักขระภาษาอังกฤษ
# (ตัวพิมพ์ใหญ่) มาเป็นคีย์ดําเนินการ โดยใช้ค่ารหัส ASCII ของอักขระตัวแรกและตัวสุดท้าย
first, last = get_ascii(0, school_name), get_ascii(-1, school_name)

for i in range(0, 10):
    # i = 0, หมายความว่า เริ่มจาก หมายเลขหลัก = 1
    if (i + 1) % 2:
        # นําค่ารหัส ASCII ของ char[0] มาบวกกับค่าประจําหลักของหมายเลขหลักที่หารด้วย 2 ไม่ลงตัว
        key_pass.append(first + i)
    else:
        # เอาค่ารหัส ASCII ของ char[-1] มาลบกับค่าประจําหลักของหมายเลขหลักที่หารด้วย 2 ลงตัว
        key_pass.append(last - i)

# Step 2
for value in key_pass:
    # นําชุดข้อมูลแต่ละหลักที่ได้ มาหาร len(school_name) แล้วเอาเศษ
    # ถ้าเศษ มากกว่า 9 ให้นำไปหาร 10 อีกรอบแล้วเอาเศษ
    pwd = value % len(school_name)
    while not 0 <= pwd <= 9:
        pwd %= 10
    gen_pass.append(pwd)

# คัดเลือกรหัสที่ถูกต้องจํานวน 6 ตัว ค่าตัวเลขประจําหลักที่อยู่กึ่งกลางชุดข้อมูล gen_pass ]
# และให้เรียงลําดับรหัสตามหมายเลขหลัก (index) จากน้อยไปมาก จากนั้นให้แสดงผลลัพธ์รหัสทางหน้าจอ
for i in range(2, 8):
    print(gen_pass[i], end=" ")
